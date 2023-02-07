'''
To some random object

              A                                     B(Attacker)

           Create
              |
              v
           Action                                     Action
(Proof of Exist, usually GET)     -->   (GET/UPDATE etc., attack behavior)
                                                        |
           Destroy                <----------------------


Assert:
- USER_A_CREDENTIAL = user_credential('test-1', 'test')
  USER_B_CREDENTIAL = user_credential('test-2', 'test')
  Two identities were created


'''
from __future__ import print_function
import pickle
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint, pformat
import logging

__logging = logging.getLogger(__name__)

import swagger_client.models

import json
import yaml

import inspect

import functools

import ast

import requests

from default_parameter import default_parameter

import http.client

TEST_GROUP_PATH = 'prefix-summary-agg-group/nova.yaml/'

TARGET_HOST = 'http://<REDACTED>:8774'

KEYSTONE_TOKEN_SERVICE_HOST = 'http://<REDACTED>:5000'

def user_credential(username, password, domain='default'):
   return {'username': username, 'password': password, 'domain': domain}

USER_A_CREDENTIAL = user_credential('test-1', 'test')

USER_B_CREDENTIAL = user_credential('test-2', 'test')

def _dict_flatten_keys(obj, prefix=''):
   r = []
   for i in obj.keys():
      if type(obj[i]) == dict:
         r += [*_dict_flatten_keys(obj[i], prefix=i + '_')]
      else:
         r += [{'key_name': i, 'data': obj[i], 'key_path': prefix + i}]
   return r

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

def keystone_v3_auth_tokens(keystone_endpoint, username, password, domain_name):
   return requests.post('{}/v3/auth/tokens'.format(keystone_endpoint), 
   json=
      {
         "auth": {
            "identity": {
                  "methods": [
                     "password"
                  ],
                  "password": {
                     "user": {
                        "name": username,
                        "domain": {
                              "name": domain_name
                        },
                        "password": password
                     }
                  }
            }
         }
      }
   ).headers['X-Subject-Token']

# TODO: 
class ApiClientConfiguration(swagger_client.configuration.Configuration):
   def __init__(self) -> None:
       super().__init__()
       self.host = TARGET_HOST

def get_openstack_client_by_token(token):
   conf = ApiClientConfiguration()
   api_client = swagger_client.api_client.ApiClient(configuration=conf)
   api_client.set_default_header('X-Auth-Token', token)

   return api_client

def operation_tag_to_classname(tags):
   
   def canonical_words_class_name(i):
      # is tag name santitized, not from path
      i = i.replace('-', '_').replace('{', '').replace('}', '').replace('.', '')
      i = ''.join(map(lambda x: x[0].upper() + ('' if len(x) < 2 else x[1:]), i.split('_')))
      return i + 'Api'
   
   return canonical_words_class_name('_'.join(tags))

def api_path_to_api_method(api_path): 
   split_vec = api_path.split('/')
   if split_vec[0] == '':
      split_vec = split_vec[1:]

   def canonical_words_method_name(i):
      r = []
      for j in i:
         j = j.replace('-', '_').replace('{', '').replace('}', '').replace('.', '')
         r += [j]
      return '_'.join(r)
      
   # clz_name = canonical_words_class_name(split_vec[0])
   # print(clz_name)
   method_name = canonical_words_method_name(split_vec)
   # print(method_name)

   return method_name

def filter_test_group(i):
   # filter 'len(methods) > 1' and [put/post] in methods
   r = []
   for idx, j in enumerate(i):
      # print(idx)
      # print(json.dumps(j, indent=2))
      orig = j

      k0 = list(j.keys())[0]
      j = j[k0]
      if '#' in j:
         if (len(j['#']['methods']) < 2) and \
         not (functools.reduce(
            lambda x, y: x or y, 
            map(lambda x: '{' in x and 'id' in x, j.keys()))
            ):
            continue
         r += [orig]
   return r

def model_class_name_from_parameter_name(parameter_name):
   return ''.join(map(lambda x: x[0].upper() + x[1:], parameter_name.split('_')))

def build_parameters_for_model(model_name, default_parameter_ref):
   # print(swagger_client.models.__dict__) 

   __logging.debug('Building Model: {}'.format(pformat(model_name)))

   req_model = swagger_client.models.__dict__[model_name]

   model_obj = req_model()
   
   # build parameters
   parameters = list(filter(
      lambda x: (not x[0].startswith('_')) and x[0] != 'attribute_map' and x[0] != 'swagger_types', 
      inspect.getmembers(req_model, lambda a: not inspect.isroutine(a))
   ))

   # print('req_model.swagger_types: {}'.format(req_model.swagger_types))

   for j in parameters:
      if j[0] in req_model.swagger_types:
         __logging.debug('  Building Parameter: {}'.format(pformat(j[0])))
         # Readding default parameter from config
         if model_name in default_parameter_ref:
            if j[0] in default_parameter_ref[model_name]:
               __logging.debug('paramater: {}, from default_parameter: {}'.format(j[0], default_parameter_ref[model_name][j[0]]))
               if not default_parameter_ref[model_name][j[0]] is None:
                  setattr(model_obj, j[0], default_parameter_ref[model_name][j[0]])
               # elif j[0] in model_obj.to_dict():
               continue

         data_type = req_model.swagger_types[j[0]]
         # TODO: Core default parameters
         if data_type == 'str': # TODO, should load some default parameter from config file
            setattr(model_obj, j[0], 'default_parameter_str')
         elif data_type == 'int':
            setattr(model_obj, j[0], 1) 
         elif data_type == 'Float' or data_type == 'Double':
            setattr(model_obj, j[0], 0.1)
         elif data_type == 'bool':
            setattr(model_obj, j[0], False)
         # TODO https://github.com/swagger-api/swagger-codegen/blob/b08cae9b26b0e607ef5ffe36a6648c128e8cc965/modules/swagger-codegen/src/main/java/io/swagger/codegen/languages/PythonClientCodegen.java#L671
         else:
            # print('j: {}'.format(j))
            setattr(model_obj, j[0], build_parameters_for_model(data_type, default_parameter_ref))
            # j[1](model_obj, build_parameters_for_model(data_type))
      else:
         j[1](model_obj, 'default_parameter') # TODO
   __logging.debug('model_obj: {}'.format(pformat(model_obj)))
   return model_obj

def api_call(clz_name, method_name, openstack_token, *api_args, **api_kwargs):
   __logging.debug('api_call - api_args: {}'.format(api_args))
   __logging.debug('api_call - api_kwargs: {}'.format(api_kwargs))
   api_client = get_openstack_client_by_token(openstack_token)
   api_clz_instance = swagger_client.__dict__[clz_name](api_client=api_client)
   api_method = api_clz_instance.__class__.__dict__[method_name]
   api_kwargs['_preload_content'] = False # No preload content into types. If no type provided, it alwayes return None
   
   __logging.debug('api_call - api_clz_instance, api_args, api_kwargs:{}, {}'.format(api_clz_instance, api_args, api_kwargs))
   
   api_method_call_ret = api_method(*[api_clz_instance, *api_args], **api_kwargs)
   return api_method_call_ret

def main():
   # logging.basicConfig(level=logging.INFO)
   # logging.basicConfig(level=logging.DEBUG)
   http.client.HTTPConnection.debuglevel = 1
   logging.getLogger("requests.packages.urllib3").setLevel(logging.DEBUG)
   import coloredlogs
   coloredlogs.install(level='INFO')

   # load prefix-summary-agg-group
   with open('prefix-summary-agg-group.pkl', 'rb') as f:
      prefix_summary_agg_group = pickle.load(f)

   # with open('nova_resource_path_resource_id_map.pkl', 'rb') as f:
   #    nova_resource_path_resouce_id_map = pickle.load(f)
   #    # print(nova_resource_path_resouce_id_map)

   # for i in prefix_summary_agg_group:
   i = prefix_summary_agg_group['nova.yaml']
   r = filter_test_group(i)

   default_parameter_nova = default_parameter['nova']

   count_tested_group = 0

   # print(len(list(r)))

   # iterate through all test groups
   for idx, j in enumerate(r):
      
      # print(idx, json.dumps(j, indent=2))

      # current path contains no {xxx_id}
      current_api_path = next(iter(j.keys()))
      if '{' not in current_api_path: 

         sub_api_keys = list(
            filter(
               lambda x: '{' in x, 
               iter(j[current_api_path].keys())
            )
         )

         sub_api_paths_contains_id = len(sub_api_keys) > 0

         if sub_api_paths_contains_id:
            # current path, post or put, A account
            # current path + /{xxxxx_id}, any, B account
            # print(idx, json.dumps(j, indent=2))

            path_prefix = ''

            k = next(iter(j.keys()))

            http_method = 'post'

            tags = j[k]['#']['detail'][http_method]['tags']

            api_full_path = path_prefix + k

            classname = operation_tag_to_classname(tags)
            method_name_prefix = api_path_to_api_method(api_full_path)

            __logging.info('A api_full_path: {}'.format(pformat(api_full_path)))

            count_tested_group += 1
            __logging.debug('count_tested_group = {}'.format(pformat(count_tested_group)))

            ##############################
            #  Token A -> Create Object  #
            ##############################

            openstack_token_a = keystone_v3_auth_tokens(KEYSTONE_TOKEN_SERVICE_HOST, 
               USER_A_CREDENTIAL['username'], USER_A_CREDENTIAL['password'], USER_A_CREDENTIAL['domain']
            )

            # The following client is for API metadata analysis only
            api_client = get_openstack_client_by_token(openstack_token_a) # TODO: token <- parameter
            api_clz_instance = swagger_client.__dict__[classname](api_client=api_client)
            api_method = api_clz_instance.__class__.__dict__[method_name_prefix + '_' + http_method] # TODO: PUT method 
            
            req_parameter_names = list(
                  filter(lambda x: x != 'self' and x != 'kwargs', inspect.signature(api_method).parameters.keys())
               )
            
            req_model_names = list(filter(lambda x: x.endswith('_req'), req_parameter_names))

            parameters_data = {}

            if len(req_model_names):
               for o in req_model_names:
                  # print('i: {}'.format(i))
                  req_model_name = model_class_name_from_parameter_name(o)
                  __logging.debug('req_model_name: {}'.format(pformat(req_model_name)))
                  n = build_parameters_for_model(req_model_name, default_parameter_nova)
                  # print(j)
                  parameters_data[o] = n

            __logging.info('parameters_data: {}'.format(pformat(parameters_data)))
                        
            api_args = parameters_data

               ############
               # Call API #
               ############

            try:
               api_method_call_ret = api_call(
                  openstack_token=openstack_token_a, 
                  clz_name=classname, 
                  method_name=method_name_prefix + '_' + http_method, 
                  **api_args
                  )
               # api_method_call_ret = api_method(api_clz_instance, **api_kwargs)
               __logging.info('api_method_call_ret.status: {}'.format(api_method_call_ret.status))
               r_data = json.loads(api_method_call_ret.data.decode('utf8'))
               __logging.info('r_data: {}'.format(pformat(r_data)))

            except ApiException as e:
               __logging.info('A main.py:372 ApiException: {}'.format(pformat(e)), exc_info=True)
               continue

            # TODO: capture created resource id
            __logging.debug('sub_api_keys')
            for l in sub_api_keys:
               resouce_id_keyname = l[ l.index('{') + 1 : l.index('}') ]

               __logging.debug('resouce_id_keyname: {}'.format(pformat(resouce_id_keyname)))

               r_data = ast.literal_eval(str(r_data)) # TODO: use real 'METHOD' to convert model to dict

               flatten_create_payload_keys = _dict_flatten_keys(r_data)

               # 'lcs' stands for Longest Common Substring

               lcs_sorted = sorted(
                  map(
                     lambda x: {'l': len(next(iter(lcs(resouce_id_keyname, x['key_path'])))), 'key': x},
                     flatten_create_payload_keys
                     ), 
                     key=lambda x: x['l'],
                     reverse=True
                  )

               most_likely_key = lcs_sorted[0]['key']
               __logging.debug('most_likely_key: {}'.format(pformat(most_likely_key)))

               ##############################
               #  Token B -> Access Object  #
               ##############################
               
               # TODO: http_method = 'get'

               b_http_method = 'delete'

               b_tags = j[k][l]['#']['detail'][b_http_method]['tags']

               b_api_full_path = api_full_path + l

               b_classname = operation_tag_to_classname(b_tags)
               b_method_name_prefix = api_path_to_api_method(b_api_full_path)

               __logging.info('B api_full_path: {}'.format(pformat(b_api_full_path)))

               openstack_token_b = keystone_v3_auth_tokens(KEYSTONE_TOKEN_SERVICE_HOST, 
                  USER_B_CREDENTIAL['username'], USER_B_CREDENTIAL['password'], USER_B_CREDENTIAL['domain']
               )

               # b_api_client = get_openstack_client_by_token(openstack_token_b) # TODO: token <- parameter
               # b_api_clz_instance = swagger_client.__dict__[b_classname](api_client=b_api_client)
               # b_api_method = b_api_clz_instance.__class__.__dict__[b_method_name_prefix + '_' + b_http_method]

               # parameters_data = {}

               try:
                  # b_api_method_call_ret = b_api_method(b_api_clz_instance, most_likely_key['data'], **{
                  #    '_preload_content': False
                  # })

                  b_api_method_call_ret = api_call(
                     b_classname, 
                     b_method_name_prefix + '_' + b_http_method, 
                     openstack_token_b, 
                     # **{ most_likely_key['key_name']: most_likely_key['data'] }, 
                     most_likely_key['data'], # TODO
                     )

                  __logging.info('api_method_call_ret.status: {}'.format(b_api_method_call_ret.status))
                  if len(b_api_method_call_ret.data):
                     r_data = json.loads(b_api_method_call_ret.data.decode('utf8'))
                     __logging.info('r_data: {}'.format(pformat(r_data)))
                  else:
                     __logging.debug('r_data length = 0')
                  __logging.info('possible weakness')

               except ApiException as e:
                  __logging.info('B main.py:448 ApiException: {}'.format(e), exc_info=True)
                  continue

def call_api_method_example():
   t1_clz_name = 'OsTenantNetworkApi'
   t1_method_name_prefix = 'v21_os_tenant_networks'

   openstack_token = keystone_v3_auth_tokens(KEYSTONE_TOKEN_SERVICE_HOST, 
      USER_A_CREDENTIAL['username'], USER_A_CREDENTIAL['password'], USER_A_CREDENTIAL['domain'])

   api_client = get_openstack_client_by_token(openstack_token)

   api_clz_instance = swagger_client.__dict__[t1_clz_name](api_client=api_client)
   
   api_method = api_clz_instance.__class__.__dict__[t1_method_name_prefix + '_get']

   api_kwargs = {
      '_preload_content': False, # No preload content into types. If no type provided, it alwayes return None
   }
   
   api_method_call_ret = api_method(api_clz_instance, **api_kwargs)

   __logging.debug('api_method_call_ret.status, api_method_call_ret: {}, {}'.format(api_method_call_ret.status, pformat(api_method_call_ret)))

def model_1_example():
   t1_clz_name = 'OsFloatingIpsApi'
   t1_method_name = 'v21_os_floating_ips_post'

   from swagger_client.models import FloatingIpsCreateReq
   create_req = FloatingIpsCreateReq(pool='public1')

   openstack_token_a = keystone_v3_auth_tokens(KEYSTONE_TOKEN_SERVICE_HOST, 
      USER_A_CREDENTIAL['username'], USER_A_CREDENTIAL['password'], USER_A_CREDENTIAL['domain']
   )

   r_a = api_call(t1_clz_name, t1_method_name, openstack_token_a, create_req)
   __logging.debug('r_a.data: {}'.format(pformat(r_a.data)))

   floating_ip_id = json.loads(r_a.data)['floating_ip']['id']

   t2_clz_name = 'OsFloatingIpsApi'
   t2_method_name = 'v21_os_floating_ips_floating_ip_id_delete'

   openstack_token_b = keystone_v3_auth_tokens(KEYSTONE_TOKEN_SERVICE_HOST,
      USER_B_CREDENTIAL['username'], USER_B_CREDENTIAL['password'], USER_B_CREDENTIAL['domain']
   )

   r_b = api_call(t2_clz_name, t2_method_name, openstack_token_b, floating_ip_id)
   __logging.debug('r_b.status, r_b.data: {}, {}'.format(r_b.status, pformat(r_b.data)))
   # Actually deleted, I am confused

   # cleanup
   r_c = api_call(t2_clz_name, t2_method_name, openstack_token_a, floating_ip_id)

   __logging.debug('r_c.data: {}'.format(pformat(r_c.data)))


if __name__ == '__main__':
   # model_1_example()
   main()

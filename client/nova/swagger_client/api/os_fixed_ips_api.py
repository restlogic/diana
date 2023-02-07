# coding: utf-8

"""
    Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OsFixedIpsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_fixed_ips_fixed_ip_action_post(self, fixed_ip, fixedip_post_req, **kwargs):  # noqa: E501
        """v21_os_fixed_ips_fixed_ip_action_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_fixed_ips_fixed_ip_action_post(fixed_ip, fixedip_post_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fixed_ip: The fixed IP of interest to you.  (required)
        :param FixedipPostReq fixedip_post_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_fixed_ips_fixed_ip_action_post_with_http_info(fixed_ip, fixedip_post_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_fixed_ips_fixed_ip_action_post_with_http_info(fixed_ip, fixedip_post_req, **kwargs)  # noqa: E501
            return data

    def v21_os_fixed_ips_fixed_ip_action_post_with_http_info(self, fixed_ip, fixedip_post_req, **kwargs):  # noqa: E501
        """v21_os_fixed_ips_fixed_ip_action_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_fixed_ips_fixed_ip_action_post_with_http_info(fixed_ip, fixedip_post_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fixed_ip: The fixed IP of interest to you.  (required)
        :param FixedipPostReq fixedip_post_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fixed_ip', 'fixedip_post_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_fixed_ips_fixed_ip_action_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fixed_ip' is set
        if self.api_client.client_side_validation and ('fixed_ip' not in params or
                                                       params['fixed_ip'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fixed_ip` when calling `v21_os_fixed_ips_fixed_ip_action_post`")  # noqa: E501
        # verify the required parameter 'fixedip_post_req' is set
        if self.api_client.client_side_validation and ('fixedip_post_req' not in params or
                                                       params['fixedip_post_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fixedip_post_req` when calling `v21_os_fixed_ips_fixed_ip_action_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fixed_ip' in params:
            path_params['fixed_ip'] = params['fixed_ip']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fixedip_post_req' in params:
            body_params = params['fixedip_post_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-fixed-ips/{fixed_ip}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v21_os_fixed_ips_fixed_ip_get(self, fixed_ip, **kwargs):  # noqa: E501
        """v21_os_fixed_ips_fixed_ip_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_fixed_ips_fixed_ip_get(fixed_ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fixed_ip: The fixed IP of interest to you.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_fixed_ips_fixed_ip_get_with_http_info(fixed_ip, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_fixed_ips_fixed_ip_get_with_http_info(fixed_ip, **kwargs)  # noqa: E501
            return data

    def v21_os_fixed_ips_fixed_ip_get_with_http_info(self, fixed_ip, **kwargs):  # noqa: E501
        """v21_os_fixed_ips_fixed_ip_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_fixed_ips_fixed_ip_get_with_http_info(fixed_ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fixed_ip: The fixed IP of interest to you.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fixed_ip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_fixed_ips_fixed_ip_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fixed_ip' is set
        if self.api_client.client_side_validation and ('fixed_ip' not in params or
                                                       params['fixed_ip'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fixed_ip` when calling `v21_os_fixed_ips_fixed_ip_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fixed_ip' in params:
            path_params['fixed_ip'] = params['fixed_ip']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-fixed-ips/{fixed_ip}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
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


class OsKeypairsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_keypairs_get(self, **kwargs):  # noqa: E501
        """v21_os_keypairs_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :param int limit: Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str marker: The last-seen item. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_keypairs_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_keypairs_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_keypairs_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_keypairs_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :param int limit: Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str marker: The last-seen item. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'marker']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_keypairs_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'marker' in params:
            query_params.append(('marker', params['marker']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-keypairs', 'GET',
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

    def v21_os_keypairs_keypair_name_delete(self, keypair_name, **kwargs):  # noqa: E501
        """v21_os_keypairs_keypair_name_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_keypair_name_delete(keypair_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keypair_name: The keypair name.  (required)
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_keypairs_keypair_name_delete_with_http_info(keypair_name, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_keypairs_keypair_name_delete_with_http_info(keypair_name, **kwargs)  # noqa: E501
            return data

    def v21_os_keypairs_keypair_name_delete_with_http_info(self, keypair_name, **kwargs):  # noqa: E501
        """v21_os_keypairs_keypair_name_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_keypair_name_delete_with_http_info(keypair_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keypair_name: The keypair name.  (required)
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keypair_name', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_keypairs_keypair_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keypair_name' is set
        if self.api_client.client_side_validation and ('keypair_name' not in params or
                                                       params['keypair_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keypair_name` when calling `v21_os_keypairs_keypair_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in params:
            path_params['keypair_name'] = params['keypair_name']  # noqa: E501

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-keypairs/{keypair_name}', 'DELETE',
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

    def v21_os_keypairs_keypair_name_get(self, keypair_name, **kwargs):  # noqa: E501
        """v21_os_keypairs_keypair_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_keypair_name_get(keypair_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keypair_name: The keypair name.  (required)
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_keypairs_keypair_name_get_with_http_info(keypair_name, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_keypairs_keypair_name_get_with_http_info(keypair_name, **kwargs)  # noqa: E501
            return data

    def v21_os_keypairs_keypair_name_get_with_http_info(self, keypair_name, **kwargs):  # noqa: E501
        """v21_os_keypairs_keypair_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_keypair_name_get_with_http_info(keypair_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keypair_name: The keypair name.  (required)
        :param str user_id: This allows administrative users to operate key-pairs of specified user ID. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keypair_name', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_keypairs_keypair_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keypair_name' is set
        if self.api_client.client_side_validation and ('keypair_name' not in params or
                                                       params['keypair_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keypair_name` when calling `v21_os_keypairs_keypair_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in params:
            path_params['keypair_name'] = params['keypair_name']  # noqa: E501

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-keypairs/{keypair_name}', 'GET',
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

    def v21_os_keypairs_post(self, keypairs_import_post_req, **kwargs):  # noqa: E501
        """v21_os_keypairs_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_post(keypairs_import_post_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeypairsImportPostReq keypairs_import_post_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_keypairs_post_with_http_info(keypairs_import_post_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_keypairs_post_with_http_info(keypairs_import_post_req, **kwargs)  # noqa: E501
            return data

    def v21_os_keypairs_post_with_http_info(self, keypairs_import_post_req, **kwargs):  # noqa: E501
        """v21_os_keypairs_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_keypairs_post_with_http_info(keypairs_import_post_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeypairsImportPostReq keypairs_import_post_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keypairs_import_post_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_keypairs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keypairs_import_post_req' is set
        if self.api_client.client_side_validation and ('keypairs_import_post_req' not in params or
                                                       params['keypairs_import_post_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keypairs_import_post_req` when calling `v21_os_keypairs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'keypairs_import_post_req' in params:
            body_params = params['keypairs_import_post_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-keypairs', 'POST',
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
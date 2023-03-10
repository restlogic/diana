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


class OsFloatingIpsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_floating_ips_floating_ip_id_delete(self, floating_ip_id, **kwargs):  # noqa: E501
        """v21_os_floating_ips_floating_ip_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_floating_ip_id_delete(floating_ip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str floating_ip_id: The ID of the floating IP address.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_floating_ips_floating_ip_id_delete_with_http_info(floating_ip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_floating_ips_floating_ip_id_delete_with_http_info(floating_ip_id, **kwargs)  # noqa: E501
            return data

    def v21_os_floating_ips_floating_ip_id_delete_with_http_info(self, floating_ip_id, **kwargs):  # noqa: E501
        """v21_os_floating_ips_floating_ip_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_floating_ip_id_delete_with_http_info(floating_ip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str floating_ip_id: The ID of the floating IP address.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['floating_ip_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_floating_ips_floating_ip_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'floating_ip_id' is set
        if self.api_client.client_side_validation and ('floating_ip_id' not in params or
                                                       params['floating_ip_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `floating_ip_id` when calling `v21_os_floating_ips_floating_ip_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in params:
            path_params['floating_ip_id'] = params['floating_ip_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-floating-ips/{floating_ip_id}', 'DELETE',
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

    def v21_os_floating_ips_floating_ip_id_get(self, floating_ip_id, **kwargs):  # noqa: E501
        """v21_os_floating_ips_floating_ip_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_floating_ip_id_get(floating_ip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str floating_ip_id: The ID of the floating IP address.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_floating_ips_floating_ip_id_get_with_http_info(floating_ip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_floating_ips_floating_ip_id_get_with_http_info(floating_ip_id, **kwargs)  # noqa: E501
            return data

    def v21_os_floating_ips_floating_ip_id_get_with_http_info(self, floating_ip_id, **kwargs):  # noqa: E501
        """v21_os_floating_ips_floating_ip_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_floating_ip_id_get_with_http_info(floating_ip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str floating_ip_id: The ID of the floating IP address.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['floating_ip_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_floating_ips_floating_ip_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'floating_ip_id' is set
        if self.api_client.client_side_validation and ('floating_ip_id' not in params or
                                                       params['floating_ip_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `floating_ip_id` when calling `v21_os_floating_ips_floating_ip_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in params:
            path_params['floating_ip_id'] = params['floating_ip_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-floating-ips/{floating_ip_id}', 'GET',
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

    def v21_os_floating_ips_get(self, **kwargs):  # noqa: E501
        """v21_os_floating_ips_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_floating_ips_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_floating_ips_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_floating_ips_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_floating_ips_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_floating_ips_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-floating-ips', 'GET',
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

    def v21_os_floating_ips_post(self, floating_ips_create_req, **kwargs):  # noqa: E501
        """v21_os_floating_ips_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_post(floating_ips_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FloatingIpsCreateReq floating_ips_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_floating_ips_post_with_http_info(floating_ips_create_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_floating_ips_post_with_http_info(floating_ips_create_req, **kwargs)  # noqa: E501
            return data

    def v21_os_floating_ips_post_with_http_info(self, floating_ips_create_req, **kwargs):  # noqa: E501
        """v21_os_floating_ips_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_floating_ips_post_with_http_info(floating_ips_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FloatingIpsCreateReq floating_ips_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['floating_ips_create_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_floating_ips_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'floating_ips_create_req' is set
        if self.api_client.client_side_validation and ('floating_ips_create_req' not in params or
                                                       params['floating_ips_create_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `floating_ips_create_req` when calling `v21_os_floating_ips_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'floating_ips_create_req' in params:
            body_params = params['floating_ips_create_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-floating-ips', 'POST',
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

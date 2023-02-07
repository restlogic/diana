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


class OsFlavorExtraSpecsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete(self, flavor_id, flavor_extra_spec_key, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete(flavor_id, flavor_extra_spec_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete_with_http_info(flavor_id, flavor_extra_spec_key, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete_with_http_info(flavor_id, flavor_extra_spec_key, **kwargs)  # noqa: E501
            return data

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete_with_http_info(self, flavor_id, flavor_extra_spec_key, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete_with_http_info(flavor_id, flavor_extra_spec_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flavor_id', 'flavor_extra_spec_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flavor_id' is set
        if self.api_client.client_side_validation and ('flavor_id' not in params or
                                                       params['flavor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_id` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete`")  # noqa: E501
        # verify the required parameter 'flavor_extra_spec_key' is set
        if self.api_client.client_side_validation and ('flavor_extra_spec_key' not in params or
                                                       params['flavor_extra_spec_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_extra_spec_key` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in params:
            path_params['flavor_id'] = params['flavor_id']  # noqa: E501
        if 'flavor_extra_spec_key' in params:
            path_params['flavor_extra_spec_key'] = params['flavor_extra_spec_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}', 'DELETE',
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

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get(self, flavor_id, flavor_extra_spec_key, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get(flavor_id, flavor_extra_spec_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get_with_http_info(flavor_id, flavor_extra_spec_key, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get_with_http_info(flavor_id, flavor_extra_spec_key, **kwargs)  # noqa: E501
            return data

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get_with_http_info(self, flavor_id, flavor_extra_spec_key, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get_with_http_info(flavor_id, flavor_extra_spec_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flavor_id', 'flavor_extra_spec_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flavor_id' is set
        if self.api_client.client_side_validation and ('flavor_id' not in params or
                                                       params['flavor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_id` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get`")  # noqa: E501
        # verify the required parameter 'flavor_extra_spec_key' is set
        if self.api_client.client_side_validation and ('flavor_extra_spec_key' not in params or
                                                       params['flavor_extra_spec_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_extra_spec_key` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in params:
            path_params['flavor_id'] = params['flavor_id']  # noqa: E501
        if 'flavor_extra_spec_key' in params:
            path_params['flavor_extra_spec_key'] = params['flavor_extra_spec_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}', 'GET',
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

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put(self, flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :param FlavorExtraSpecsUpdateReq flavor_extra_specs_update_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put_with_http_info(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put_with_http_info(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, **kwargs)  # noqa: E501
            return data

    def v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put_with_http_info(self, flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put_with_http_info(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param str flavor_extra_spec_key: The extra spec key for the flavor.  (required)
        :param FlavorExtraSpecsUpdateReq flavor_extra_specs_update_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flavor_id', 'flavor_extra_spec_key', 'flavor_extra_specs_update_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flavor_id' is set
        if self.api_client.client_side_validation and ('flavor_id' not in params or
                                                       params['flavor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_id` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put`")  # noqa: E501
        # verify the required parameter 'flavor_extra_spec_key' is set
        if self.api_client.client_side_validation and ('flavor_extra_spec_key' not in params or
                                                       params['flavor_extra_spec_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_extra_spec_key` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put`")  # noqa: E501
        # verify the required parameter 'flavor_extra_specs_update_req' is set
        if self.api_client.client_side_validation and ('flavor_extra_specs_update_req' not in params or
                                                       params['flavor_extra_specs_update_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_extra_specs_update_req` when calling `v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in params:
            path_params['flavor_id'] = params['flavor_id']  # noqa: E501
        if 'flavor_extra_spec_key' in params:
            path_params['flavor_extra_spec_key'] = params['flavor_extra_spec_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'flavor_extra_specs_update_req' in params:
            body_params = params['flavor_extra_specs_update_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}', 'PUT',
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

    def v21_flavors_flavor_id_os_extra_specs_get(self, flavor_id, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_get(flavor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_flavors_flavor_id_os_extra_specs_get_with_http_info(flavor_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_flavors_flavor_id_os_extra_specs_get_with_http_info(flavor_id, **kwargs)  # noqa: E501
            return data

    def v21_flavors_flavor_id_os_extra_specs_get_with_http_info(self, flavor_id, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_get_with_http_info(flavor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flavor_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_flavors_flavor_id_os_extra_specs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flavor_id' is set
        if self.api_client.client_side_validation and ('flavor_id' not in params or
                                                       params['flavor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_id` when calling `v21_flavors_flavor_id_os_extra_specs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in params:
            path_params['flavor_id'] = params['flavor_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/flavors/{flavor_id}/os-extra_specs', 'GET',
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

    def v21_flavors_flavor_id_os_extra_specs_post(self, flavor_id, flavor_extra_specs_create_req, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_post(flavor_id, flavor_extra_specs_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param FlavorExtraSpecsCreateReq flavor_extra_specs_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_flavors_flavor_id_os_extra_specs_post_with_http_info(flavor_id, flavor_extra_specs_create_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_flavors_flavor_id_os_extra_specs_post_with_http_info(flavor_id, flavor_extra_specs_create_req, **kwargs)  # noqa: E501
            return data

    def v21_flavors_flavor_id_os_extra_specs_post_with_http_info(self, flavor_id, flavor_extra_specs_create_req, **kwargs):  # noqa: E501
        """v21_flavors_flavor_id_os_extra_specs_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_flavors_flavor_id_os_extra_specs_post_with_http_info(flavor_id, flavor_extra_specs_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flavor_id: The ID of the flavor.  (required)
        :param FlavorExtraSpecsCreateReq flavor_extra_specs_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flavor_id', 'flavor_extra_specs_create_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_flavors_flavor_id_os_extra_specs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flavor_id' is set
        if self.api_client.client_side_validation and ('flavor_id' not in params or
                                                       params['flavor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_id` when calling `v21_flavors_flavor_id_os_extra_specs_post`")  # noqa: E501
        # verify the required parameter 'flavor_extra_specs_create_req' is set
        if self.api_client.client_side_validation and ('flavor_extra_specs_create_req' not in params or
                                                       params['flavor_extra_specs_create_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flavor_extra_specs_create_req` when calling `v21_flavors_flavor_id_os_extra_specs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in params:
            path_params['flavor_id'] = params['flavor_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'flavor_extra_specs_create_req' in params:
            body_params = params['flavor_extra_specs_create_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/flavors/{flavor_id}/os-extra_specs', 'POST',
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

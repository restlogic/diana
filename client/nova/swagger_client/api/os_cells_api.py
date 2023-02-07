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


class OsCellsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_cells_capacities_get(self, **kwargs):  # noqa: E501
        """v21_os_cells_capacities_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_capacities_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_capacities_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_capacities_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_capacities_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_capacities_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_capacities_get_with_http_info(async_req=True)
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
                    " to method v21_os_cells_capacities_get" % key
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
            '/v2.1/os-cells/capacities', 'GET',
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

    def v21_os_cells_cell_id_capacities_get(self, cell_id, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_capacities_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_capacities_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cell_id: The UUID of the cell.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_cell_id_capacities_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_cell_id_capacities_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def v21_os_cells_cell_id_capacities_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_capacities_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_capacities_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cell_id: The UUID of the cell.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cells_cell_id_capacities_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `v21_os_cells_cell_id_capacities_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cell_id' in params:
            path_params['cell_id'] = params['cell_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cells/{cell_id}/capacities', 'GET',
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

    def v21_os_cells_cell_id_delete(self, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_cell_id_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_cell_id_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_cell_id_delete_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_delete_with_http_info(async_req=True)
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
                    " to method v21_os_cells_cell_id_delete" % key
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
            '/v2.1/os-cells/{cell_id}', 'DELETE',
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

    def v21_os_cells_cell_id_get(self, cell_id, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cell_id: The UUID of the cell.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_cell_id_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_cell_id_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def v21_os_cells_cell_id_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cell_id: The UUID of the cell.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cells_cell_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `v21_os_cells_cell_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cell_id' in params:
            path_params['cell_id'] = params['cell_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cells/{cell_id}', 'GET',
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

    def v21_os_cells_cell_id_put(self, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_cell_id_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_cell_id_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_cell_id_put_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_cell_id_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_cell_id_put_with_http_info(async_req=True)
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
                    " to method v21_os_cells_cell_id_put" % key
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
            '/v2.1/os-cells/{cell_id}', 'PUT',
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

    def v21_os_cells_detail_get(self, **kwargs):  # noqa: E501
        """v21_os_cells_detail_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead. 
        :param int offset: Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_detail_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead. 
        :param int offset: Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cells_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cells/detail', 'GET',
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

    def v21_os_cells_get(self, **kwargs):  # noqa: E501
        """v21_os_cells_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead. 
        :param int offset: Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead. 
        :param int offset: Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cells_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cells', 'GET',
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

    def v21_os_cells_info_get(self, **kwargs):  # noqa: E501
        """v21_os_cells_info_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_info_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_info_get_with_http_info(async_req=True)
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
                    " to method v21_os_cells_info_get" % key
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
            '/v2.1/os-cells/info', 'GET',
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

    def v21_os_cells_post(self, **kwargs):  # noqa: E501
        """v21_os_cells_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cells_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cells_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cells_post_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cells_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cells_post_with_http_info(async_req=True)
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
                    " to method v21_os_cells_post" % key
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
            '/v2.1/os-cells', 'POST',
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

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


class OsInstanceActionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_servers_server_id_os_instance_actions_get(self, server_id, **kwargs):  # noqa: E501
        """v21_servers_server_id_os_instance_actions_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_servers_server_id_os_instance_actions_get(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The UUID of the server.  (required)
        :param int limit: Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str marker: The ``request_id`` of the last-seen instance action. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str changes_since: Filters the response by a date and time stamp when the instance action last changed.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss??hh:mm  The ``??hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400. 
        :param str changes_before: Filters the response by a date and time stamp when the instance actions last changed. Those instances that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss??hh:mm  The ``??hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_servers_server_id_os_instance_actions_get_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_servers_server_id_os_instance_actions_get_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def v21_servers_server_id_os_instance_actions_get_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """v21_servers_server_id_os_instance_actions_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_servers_server_id_os_instance_actions_get_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The UUID of the server.  (required)
        :param int limit: Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str marker: The ``request_id`` of the last-seen instance action. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request. 
        :param str changes_since: Filters the response by a date and time stamp when the instance action last changed.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss??hh:mm  The ``??hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400. 
        :param str changes_before: Filters the response by a date and time stamp when the instance actions last changed. Those instances that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss??hh:mm  The ``??hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'limit', 'marker', 'changes_since', 'changes_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_servers_server_id_os_instance_actions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in params or
                                                       params['server_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `server_id` when calling `v21_servers_server_id_os_instance_actions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'marker' in params:
            query_params.append(('marker', params['marker']))  # noqa: E501
        if 'changes_since' in params:
            query_params.append(('changes-since', params['changes_since']))  # noqa: E501
        if 'changes_before' in params:
            query_params.append(('changes-before', params['changes_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/servers/{server_id}/os-instance-actions', 'GET',
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

    def v21_servers_server_id_os_instance_actions_request_id_get(self, server_id, request_id, **kwargs):  # noqa: E501
        """v21_servers_server_id_os_instance_actions_request_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_servers_server_id_os_instance_actions_request_id_get(server_id, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The UUID of the server.  (required)
        :param str request_id: The ID of the request.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_servers_server_id_os_instance_actions_request_id_get_with_http_info(server_id, request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_servers_server_id_os_instance_actions_request_id_get_with_http_info(server_id, request_id, **kwargs)  # noqa: E501
            return data

    def v21_servers_server_id_os_instance_actions_request_id_get_with_http_info(self, server_id, request_id, **kwargs):  # noqa: E501
        """v21_servers_server_id_os_instance_actions_request_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_servers_server_id_os_instance_actions_request_id_get_with_http_info(server_id, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The UUID of the server.  (required)
        :param str request_id: The ID of the request.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_servers_server_id_os_instance_actions_request_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in params or
                                                       params['server_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `server_id` when calling `v21_servers_server_id_os_instance_actions_request_id_get`")  # noqa: E501
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in params or
                                                       params['request_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request_id` when calling `v21_servers_server_id_os_instance_actions_request_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'request_id' in params:
            path_params['request_id'] = params['request_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/servers/{server_id}/os-instance-actions/{request_id}', 'GET',
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

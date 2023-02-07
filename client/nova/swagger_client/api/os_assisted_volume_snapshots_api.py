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


class OsAssistedVolumeSnapshotsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_assisted_volume_snapshots_post(self, snapshot_create_assisted_req, **kwargs):  # noqa: E501
        """v21_os_assisted_volume_snapshots_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_assisted_volume_snapshots_post(snapshot_create_assisted_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotCreateAssistedReq snapshot_create_assisted_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_assisted_volume_snapshots_post_with_http_info(snapshot_create_assisted_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_assisted_volume_snapshots_post_with_http_info(snapshot_create_assisted_req, **kwargs)  # noqa: E501
            return data

    def v21_os_assisted_volume_snapshots_post_with_http_info(self, snapshot_create_assisted_req, **kwargs):  # noqa: E501
        """v21_os_assisted_volume_snapshots_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_assisted_volume_snapshots_post_with_http_info(snapshot_create_assisted_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotCreateAssistedReq snapshot_create_assisted_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_create_assisted_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_assisted_volume_snapshots_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_create_assisted_req' is set
        if self.api_client.client_side_validation and ('snapshot_create_assisted_req' not in params or
                                                       params['snapshot_create_assisted_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `snapshot_create_assisted_req` when calling `v21_os_assisted_volume_snapshots_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'snapshot_create_assisted_req' in params:
            body_params = params['snapshot_create_assisted_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-assisted-volume-snapshots', 'POST',
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

    def v21_os_assisted_volume_snapshots_snapshot_id_delete(self, snapshot_id, delete_info, **kwargs):  # noqa: E501
        """v21_os_assisted_volume_snapshots_snapshot_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_assisted_volume_snapshots_snapshot_id_delete(snapshot_id, delete_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_id: The UUID of the snapshot.  (required)
        :param str delete_info: Information for snapshot deletion. Include the ID of the associated volume. For example:  .. code-block:: javascript     DELETE /os-assisted-volume-snapshots/421752a6-acf6-4b2d-bc7a-119f9148cd8c?delete_info='{\"volume_id\": \"521752a6-acf6-4b2d-bc7a-119f9148cd8c\"}'  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_assisted_volume_snapshots_snapshot_id_delete_with_http_info(snapshot_id, delete_info, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_assisted_volume_snapshots_snapshot_id_delete_with_http_info(snapshot_id, delete_info, **kwargs)  # noqa: E501
            return data

    def v21_os_assisted_volume_snapshots_snapshot_id_delete_with_http_info(self, snapshot_id, delete_info, **kwargs):  # noqa: E501
        """v21_os_assisted_volume_snapshots_snapshot_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_assisted_volume_snapshots_snapshot_id_delete_with_http_info(snapshot_id, delete_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_id: The UUID of the snapshot.  (required)
        :param str delete_info: Information for snapshot deletion. Include the ID of the associated volume. For example:  .. code-block:: javascript     DELETE /os-assisted-volume-snapshots/421752a6-acf6-4b2d-bc7a-119f9148cd8c?delete_info='{\"volume_id\": \"521752a6-acf6-4b2d-bc7a-119f9148cd8c\"}'  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_id', 'delete_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_assisted_volume_snapshots_snapshot_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_id' is set
        if self.api_client.client_side_validation and ('snapshot_id' not in params or
                                                       params['snapshot_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `snapshot_id` when calling `v21_os_assisted_volume_snapshots_snapshot_id_delete`")  # noqa: E501
        # verify the required parameter 'delete_info' is set
        if self.api_client.client_side_validation and ('delete_info' not in params or
                                                       params['delete_info'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `delete_info` when calling `v21_os_assisted_volume_snapshots_snapshot_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in params:
            path_params['snapshot_id'] = params['snapshot_id']  # noqa: E501

        query_params = []
        if 'delete_info' in params:
            query_params.append(('delete_info', params['delete_info']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-assisted-volume-snapshots/{snapshot_id}', 'DELETE',
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

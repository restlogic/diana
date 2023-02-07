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


class OsCloudpipeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v21_os_cloudpipe_configure_project_put(self, cloud_pipe_update_req, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_configure_project_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_configure_project_put(cloud_pipe_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudPipeUpdateReq cloud_pipe_update_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cloudpipe_configure_project_put_with_http_info(cloud_pipe_update_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cloudpipe_configure_project_put_with_http_info(cloud_pipe_update_req, **kwargs)  # noqa: E501
            return data

    def v21_os_cloudpipe_configure_project_put_with_http_info(self, cloud_pipe_update_req, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_configure_project_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_configure_project_put_with_http_info(cloud_pipe_update_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudPipeUpdateReq cloud_pipe_update_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_pipe_update_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cloudpipe_configure_project_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_pipe_update_req' is set
        if self.api_client.client_side_validation and ('cloud_pipe_update_req' not in params or
                                                       params['cloud_pipe_update_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_pipe_update_req` when calling `v21_os_cloudpipe_configure_project_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cloud_pipe_update_req' in params:
            body_params = params['cloud_pipe_update_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cloudpipe/configure-project', 'PUT',
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

    def v21_os_cloudpipe_get(self, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cloudpipe_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cloudpipe_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v21_os_cloudpipe_get_with_http_info(self, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_get_with_http_info(async_req=True)
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
                    " to method v21_os_cloudpipe_get" % key
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
            '/v2.1/os-cloudpipe', 'GET',
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

    def v21_os_cloudpipe_post(self, cloud_pipe_create_req, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_post(cloud_pipe_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudPipeCreateReq cloud_pipe_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v21_os_cloudpipe_post_with_http_info(cloud_pipe_create_req, **kwargs)  # noqa: E501
        else:
            (data) = self.v21_os_cloudpipe_post_with_http_info(cloud_pipe_create_req, **kwargs)  # noqa: E501
            return data

    def v21_os_cloudpipe_post_with_http_info(self, cloud_pipe_create_req, **kwargs):  # noqa: E501
        """v21_os_cloudpipe_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v21_os_cloudpipe_post_with_http_info(cloud_pipe_create_req, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudPipeCreateReq cloud_pipe_create_req: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_pipe_create_req']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v21_os_cloudpipe_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_pipe_create_req' is set
        if self.api_client.client_side_validation and ('cloud_pipe_create_req' not in params or
                                                       params['cloud_pipe_create_req'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_pipe_create_req` when calling `v21_os_cloudpipe_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cloud_pipe_create_req' in params:
            body_params = params['cloud_pipe_create_req']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/os-cloudpipe', 'POST',
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

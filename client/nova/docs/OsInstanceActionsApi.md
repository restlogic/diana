# swagger_client.OsInstanceActionsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_os_instance_actions_get**](OsInstanceActionsApi.md#v21_servers_server_id_os_instance_actions_get) | **GET** /v2.1/servers/{server_id}/os-instance-actions | 
[**v21_servers_server_id_os_instance_actions_request_id_get**](OsInstanceActionsApi.md#v21_servers_server_id_os_instance_actions_request_id_get) | **GET** /v2.1/servers/{server_id}/os-instance-actions/{request_id} | 


# **v21_servers_server_id_os_instance_actions_get**
> v21_servers_server_id_os_instance_actions_get(server_id, limit=limit, marker=marker, changes_since=changes_since, changes_before=changes_before)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInstanceActionsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The ``request_id`` of the last-seen instance action. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
changes_since = 'changes_since_example' # str | Filters the response by a date and time stamp when the instance action last changed.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400.  (optional)
changes_before = 'changes_before_example' # str | Filters the response by a date and time stamp when the instance actions last changed. Those instances that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400.  (optional)

try:
    api_instance.v21_servers_server_id_os_instance_actions_get(server_id, limit=limit, marker=marker, changes_since=changes_since, changes_before=changes_before)
except ApiException as e:
    print("Exception when calling OsInstanceActionsApi->v21_servers_server_id_os_instance_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The &#x60;&#x60;request_id&#x60;&#x60; of the last-seen instance action. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **changes_since** | **str**| Filters the response by a date and time stamp when the instance action last changed.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-since&#x60;&#x60; must be earlier than or equal to the value of the &#x60;&#x60;changes-before&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **changes_before** | **str**| Filters the response by a date and time stamp when the instance actions last changed. Those instances that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-before&#x60;&#x60; must be later than or equal to the value of the &#x60;&#x60;changes-since&#x60;&#x60; otherwise API will return 400.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_instance_actions_request_id_get**
> v21_servers_server_id_os_instance_actions_request_id_get(server_id, request_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInstanceActionsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
request_id = 'request_id_example' # str | The ID of the request. 

try:
    api_instance.v21_servers_server_id_os_instance_actions_request_id_get(server_id, request_id)
except ApiException as e:
    print("Exception when calling OsInstanceActionsApi->v21_servers_server_id_os_instance_actions_request_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **request_id** | **str**| The ID of the request.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


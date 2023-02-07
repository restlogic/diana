# swagger_client.OsVirtualInterfacesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_os_virtual_interfaces_get**](OsVirtualInterfacesApi.md#v21_servers_server_id_os_virtual_interfaces_get) | **GET** /v2.1/servers/{server_id}/os-virtual-interfaces | 


# **v21_servers_server_id_os_virtual_interfaces_get**
> v21_servers_server_id_os_virtual_interfaces_get(server_id, limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVirtualInterfacesApi()
server_id = 'server_id_example' # str | The UUID of the server. 
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_servers_server_id_os_virtual_interfaces_get(server_id, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVirtualInterfacesApi->v21_servers_server_id_os_virtual_interfaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **limit** | **int**| Used in conjunction with &#x60;&#x60;offset&#x60;&#x60; to return a slice of items. &#x60;&#x60;limit&#x60;&#x60; is the maximum number of items to return. If &#x60;&#x60;limit&#x60;&#x60; is not specified, or exceeds the configurable &#x60;&#x60;max_limit&#x60;&#x60;, then &#x60;&#x60;max_limit&#x60;&#x60; will be used instead.  | [optional] 
 **offset** | **int**| Used in conjunction with &#x60;&#x60;limit&#x60;&#x60; to return a slice of items. &#x60;&#x60;offset&#x60;&#x60; is where to start in the list.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


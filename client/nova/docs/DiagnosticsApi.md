# swagger_client.DiagnosticsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_diagnostics_get**](DiagnosticsApi.md#v21_servers_server_id_diagnostics_get) | **GET** /v2.1/servers/{server_id}/diagnostics | 


# **v21_servers_server_id_diagnostics_get**
> v21_servers_server_id_diagnostics_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiagnosticsApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_diagnostics_get(server_id)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->v21_servers_server_id_diagnostics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


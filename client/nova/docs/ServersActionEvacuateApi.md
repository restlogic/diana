# swagger_client.ServersActionEvacuateApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_action_post**](ServersActionEvacuateApi.md#v21_servers_server_id_action_post) | **POST** /v2.1/servers/{server_id}/action | 


# **v21_servers_server_id_action_post**
> v21_servers_server_id_action_post(server_id, server_evacuate_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersActionEvacuateApi()
server_id = 'server_id_example' # str | The UUID of the server. 
server_evacuate_req = swagger_client.ServerEvacuateReq() # ServerEvacuateReq | 

try:
    api_instance.v21_servers_server_id_action_post(server_id, server_evacuate_req)
except ApiException as e:
    print("Exception when calling ServersActionEvacuateApi->v21_servers_server_id_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **server_evacuate_req** | [**ServerEvacuateReq**](ServerEvacuateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


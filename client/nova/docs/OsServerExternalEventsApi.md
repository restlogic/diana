# swagger_client.OsServerExternalEventsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_server_external_events_post**](OsServerExternalEventsApi.md#v21_os_server_external_events_post) | **POST** /v2.1/os-server-external-events | 


# **v21_os_server_external_events_post**
> v21_os_server_external_events_post(event_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerExternalEventsApi()
event_create_req = swagger_client.EventCreateReq() # EventCreateReq | 

try:
    api_instance.v21_os_server_external_events_post(event_create_req)
except ApiException as e:
    print("Exception when calling OsServerExternalEventsApi->v21_os_server_external_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_create_req** | [**EventCreateReq**](EventCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


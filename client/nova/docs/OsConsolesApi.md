# swagger_client.OsConsolesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_consoles_console_id_delete**](OsConsolesApi.md#v21_servers_server_id_consoles_console_id_delete) | **DELETE** /v2.1/servers/{server_id}/consoles/{console_id} | 
[**v21_servers_server_id_consoles_console_id_get**](OsConsolesApi.md#v21_servers_server_id_consoles_console_id_get) | **GET** /v2.1/servers/{server_id}/consoles/{console_id} | 
[**v21_servers_server_id_consoles_get**](OsConsolesApi.md#v21_servers_server_id_consoles_get) | **GET** /v2.1/servers/{server_id}/consoles | 
[**v21_servers_server_id_consoles_post**](OsConsolesApi.md#v21_servers_server_id_consoles_post) | **POST** /v2.1/servers/{server_id}/consoles | 


# **v21_servers_server_id_consoles_console_id_delete**
> v21_servers_server_id_consoles_console_id_delete(server_id, console_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsConsolesApi()
server_id = 'server_id_example' # str | The UUID of the server. 
console_id = 'console_id_example' # str | The UUID of the console. 

try:
    api_instance.v21_servers_server_id_consoles_console_id_delete(server_id, console_id)
except ApiException as e:
    print("Exception when calling OsConsolesApi->v21_servers_server_id_consoles_console_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **console_id** | **str**| The UUID of the console.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_consoles_console_id_get**
> v21_servers_server_id_consoles_console_id_get(server_id, console_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsConsolesApi()
server_id = 'server_id_example' # str | The UUID of the server. 
console_id = 'console_id_example' # str | The UUID of the console. 

try:
    api_instance.v21_servers_server_id_consoles_console_id_get(server_id, console_id)
except ApiException as e:
    print("Exception when calling OsConsolesApi->v21_servers_server_id_consoles_console_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **console_id** | **str**| The UUID of the console.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_consoles_get**
> v21_servers_server_id_consoles_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsConsolesApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_consoles_get(server_id)
except ApiException as e:
    print("Exception when calling OsConsolesApi->v21_servers_server_id_consoles_get: %s\n" % e)
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

# **v21_servers_server_id_consoles_post**
> v21_servers_server_id_consoles_post(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsConsolesApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_consoles_post(server_id)
except ApiException as e:
    print("Exception when calling OsConsolesApi->v21_servers_server_id_consoles_post: %s\n" % e)
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


# swagger_client.MetadataApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_metadata_get**](MetadataApi.md#v21_servers_server_id_metadata_get) | **GET** /v2.1/servers/{server_id}/metadata | 
[**v21_servers_server_id_metadata_key_delete**](MetadataApi.md#v21_servers_server_id_metadata_key_delete) | **DELETE** /v2.1/servers/{server_id}/metadata/{key} | 
[**v21_servers_server_id_metadata_key_get**](MetadataApi.md#v21_servers_server_id_metadata_key_get) | **GET** /v2.1/servers/{server_id}/metadata/{key} | 
[**v21_servers_server_id_metadata_key_put**](MetadataApi.md#v21_servers_server_id_metadata_key_put) | **PUT** /v2.1/servers/{server_id}/metadata/{key} | 
[**v21_servers_server_id_metadata_post**](MetadataApi.md#v21_servers_server_id_metadata_post) | **POST** /v2.1/servers/{server_id}/metadata | 
[**v21_servers_server_id_metadata_put**](MetadataApi.md#v21_servers_server_id_metadata_put) | **PUT** /v2.1/servers/{server_id}/metadata | 


# **v21_servers_server_id_metadata_get**
> v21_servers_server_id_metadata_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_metadata_get(server_id)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_get: %s\n" % e)
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

# **v21_servers_server_id_metadata_key_delete**
> v21_servers_server_id_metadata_key_delete(server_id, key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 

try:
    api_instance.v21_servers_server_id_metadata_key_delete(server_id, key)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_metadata_key_get**
> v21_servers_server_id_metadata_key_get(server_id, key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 

try:
    api_instance.v21_servers_server_id_metadata_key_get(server_id, key)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_metadata_key_put**
> v21_servers_server_id_metadata_key_put(server_id, key, server_metadata_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 
server_metadata_req = swagger_client.ServerMetadataReq() # ServerMetadataReq | 

try:
    api_instance.v21_servers_server_id_metadata_key_put(server_id, key, server_metadata_req)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 
 **server_metadata_req** | [**ServerMetadataReq**](ServerMetadataReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_metadata_post**
> v21_servers_server_id_metadata_post(server_id, server_metadata_all_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 
server_metadata_all_req = swagger_client.ServerMetadataAllReq() # ServerMetadataAllReq | 

try:
    api_instance.v21_servers_server_id_metadata_post(server_id, server_metadata_all_req)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **server_metadata_all_req** | [**ServerMetadataAllReq**](ServerMetadataAllReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_metadata_put**
> v21_servers_server_id_metadata_put(server_id, server_metadata_all_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
server_id = 'server_id_example' # str | The UUID of the server. 
server_metadata_all_req = swagger_client.ServerMetadataAllReq() # ServerMetadataAllReq | 

try:
    api_instance.v21_servers_server_id_metadata_put(server_id, server_metadata_all_req)
except ApiException as e:
    print("Exception when calling MetadataApi->v21_servers_server_id_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **server_metadata_all_req** | [**ServerMetadataAllReq**](ServerMetadataAllReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


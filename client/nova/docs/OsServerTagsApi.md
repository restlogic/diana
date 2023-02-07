# swagger_client.OsServerTagsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_tags_delete**](OsServerTagsApi.md#v21_servers_server_id_tags_delete) | **DELETE** /v2.1/servers/{server_id}/tags | 
[**v21_servers_server_id_tags_get**](OsServerTagsApi.md#v21_servers_server_id_tags_get) | **GET** /v2.1/servers/{server_id}/tags | 
[**v21_servers_server_id_tags_put**](OsServerTagsApi.md#v21_servers_server_id_tags_put) | **PUT** /v2.1/servers/{server_id}/tags | 
[**v21_servers_server_id_tags_tag_delete**](OsServerTagsApi.md#v21_servers_server_id_tags_tag_delete) | **DELETE** /v2.1/servers/{server_id}/tags/{tag} | 
[**v21_servers_server_id_tags_tag_get**](OsServerTagsApi.md#v21_servers_server_id_tags_tag_get) | **GET** /v2.1/servers/{server_id}/tags/{tag} | 
[**v21_servers_server_id_tags_tag_put**](OsServerTagsApi.md#v21_servers_server_id_tags_tag_put) | **PUT** /v2.1/servers/{server_id}/tags/{tag} | 


# **v21_servers_server_id_tags_delete**
> v21_servers_server_id_tags_delete(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_tags_delete(server_id)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_delete: %s\n" % e)
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

# **v21_servers_server_id_tags_get**
> v21_servers_server_id_tags_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_tags_get(server_id)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_get: %s\n" % e)
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

# **v21_servers_server_id_tags_put**
> v21_servers_server_id_tags_put(server_id, server_tags_put_all_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
server_tags_put_all_req = swagger_client.ServerTagsPutAllReq() # ServerTagsPutAllReq | 

try:
    api_instance.v21_servers_server_id_tags_put(server_id, server_tags_put_all_req)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **server_tags_put_all_req** | [**ServerTagsPutAllReq**](ServerTagsPutAllReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_tags_tag_delete**
> v21_servers_server_id_tags_tag_delete(server_id, tag)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
tag = 'tag_example' # str | The tag as a string. 

try:
    api_instance.v21_servers_server_id_tags_tag_delete(server_id, tag)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **tag** | **str**| The tag as a string.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_tags_tag_get**
> v21_servers_server_id_tags_tag_get(server_id, tag)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
tag = 'tag_example' # str | The tag as a string. 

try:
    api_instance.v21_servers_server_id_tags_tag_get(server_id, tag)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **tag** | **str**| The tag as a string.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_tags_tag_put**
> v21_servers_server_id_tags_tag_put(server_id, tag)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerTagsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
tag = 'tag_example' # str | The tag as a string. 

try:
    api_instance.v21_servers_server_id_tags_tag_put(server_id, tag)
except ApiException as e:
    print("Exception when calling OsServerTagsApi->v21_servers_server_id_tags_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **tag** | **str**| The tag as a string.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


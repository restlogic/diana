# swagger_client.OsAggregatesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_aggregates_aggregate_id_action_post**](OsAggregatesApi.md#v21_os_aggregates_aggregate_id_action_post) | **POST** /v2.1/os-aggregates/{aggregate_id}/action | 
[**v21_os_aggregates_aggregate_id_delete**](OsAggregatesApi.md#v21_os_aggregates_aggregate_id_delete) | **DELETE** /v2.1/os-aggregates/{aggregate_id} | 
[**v21_os_aggregates_aggregate_id_get**](OsAggregatesApi.md#v21_os_aggregates_aggregate_id_get) | **GET** /v2.1/os-aggregates/{aggregate_id} | 
[**v21_os_aggregates_aggregate_id_images_post**](OsAggregatesApi.md#v21_os_aggregates_aggregate_id_images_post) | **POST** /v2.1/os-aggregates/{aggregate_id}/images | 
[**v21_os_aggregates_aggregate_id_put**](OsAggregatesApi.md#v21_os_aggregates_aggregate_id_put) | **PUT** /v2.1/os-aggregates/{aggregate_id} | 
[**v21_os_aggregates_get**](OsAggregatesApi.md#v21_os_aggregates_get) | **GET** /v2.1/os-aggregates | 
[**v21_os_aggregates_post**](OsAggregatesApi.md#v21_os_aggregates_post) | **POST** /v2.1/os-aggregates | 


# **v21_os_aggregates_aggregate_id_action_post**
> v21_os_aggregates_aggregate_id_action_post(aggregate_id, aggregate_add_host_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_id = 56 # int | The aggregate ID. 
aggregate_add_host_post_req = swagger_client.AggregateAddHostPostReq() # AggregateAddHostPostReq | 

try:
    api_instance.v21_os_aggregates_aggregate_id_action_post(aggregate_id, aggregate_add_host_post_req)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_aggregate_id_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_id** | **int**| The aggregate ID.  | 
 **aggregate_add_host_post_req** | [**AggregateAddHostPostReq**](AggregateAddHostPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_aggregate_id_delete**
> v21_os_aggregates_aggregate_id_delete(aggregate_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_id = 56 # int | The aggregate ID. 

try:
    api_instance.v21_os_aggregates_aggregate_id_delete(aggregate_id)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_aggregate_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_id** | **int**| The aggregate ID.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_aggregate_id_get**
> v21_os_aggregates_aggregate_id_get(aggregate_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_id = 56 # int | The aggregate ID. 

try:
    api_instance.v21_os_aggregates_aggregate_id_get(aggregate_id)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_aggregate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_id** | **int**| The aggregate ID.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_aggregate_id_images_post**
> v21_os_aggregates_aggregate_id_images_post(aggregate_id, aggregate_images_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_id = 56 # int | The aggregate ID. 
aggregate_images_post_req = swagger_client.AggregateImagesPostReq() # AggregateImagesPostReq | 

try:
    api_instance.v21_os_aggregates_aggregate_id_images_post(aggregate_id, aggregate_images_post_req)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_aggregate_id_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_id** | **int**| The aggregate ID.  | 
 **aggregate_images_post_req** | [**AggregateImagesPostReq**](AggregateImagesPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_aggregate_id_put**
> v21_os_aggregates_aggregate_id_put(aggregate_id, aggregate_update_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_id = 56 # int | The aggregate ID. 
aggregate_update_post_req = swagger_client.AggregateUpdatePostReq() # AggregateUpdatePostReq | 

try:
    api_instance.v21_os_aggregates_aggregate_id_put(aggregate_id, aggregate_update_post_req)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_aggregate_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_id** | **int**| The aggregate ID.  | 
 **aggregate_update_post_req** | [**AggregateUpdatePostReq**](AggregateUpdatePostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_get**
> v21_os_aggregates_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()

try:
    api_instance.v21_os_aggregates_get()
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_aggregates_post**
> v21_os_aggregates_post(aggregate_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAggregatesApi()
aggregate_post_req = swagger_client.AggregatePostReq() # AggregatePostReq | 

try:
    api_instance.v21_os_aggregates_post(aggregate_post_req)
except ApiException as e:
    print("Exception when calling OsAggregatesApi->v21_os_aggregates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_post_req** | [**AggregatePostReq**](AggregatePostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


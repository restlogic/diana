# swagger_client.OsKeypairsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_keypairs_get**](OsKeypairsApi.md#v21_os_keypairs_get) | **GET** /v2.1/os-keypairs | 
[**v21_os_keypairs_keypair_name_delete**](OsKeypairsApi.md#v21_os_keypairs_keypair_name_delete) | **DELETE** /v2.1/os-keypairs/{keypair_name} | 
[**v21_os_keypairs_keypair_name_get**](OsKeypairsApi.md#v21_os_keypairs_keypair_name_get) | **GET** /v2.1/os-keypairs/{keypair_name} | 
[**v21_os_keypairs_post**](OsKeypairsApi.md#v21_os_keypairs_post) | **POST** /v2.1/os-keypairs | 


# **v21_os_keypairs_get**
> v21_os_keypairs_get(user_id=user_id, limit=limit, marker=marker)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsKeypairsApi()
user_id = 'user_id_example' # str | This allows administrative users to operate key-pairs of specified user ID.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The last-seen item. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)

try:
    api_instance.v21_os_keypairs_get(user_id=user_id, limit=limit, marker=marker)
except ApiException as e:
    print("Exception when calling OsKeypairsApi->v21_os_keypairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This allows administrative users to operate key-pairs of specified user ID.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_keypairs_keypair_name_delete**
> v21_os_keypairs_keypair_name_delete(keypair_name, user_id=user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsKeypairsApi()
keypair_name = 'keypair_name_example' # str | The keypair name. 
user_id = 'user_id_example' # str | This allows administrative users to operate key-pairs of specified user ID.  (optional)

try:
    api_instance.v21_os_keypairs_keypair_name_delete(keypair_name, user_id=user_id)
except ApiException as e:
    print("Exception when calling OsKeypairsApi->v21_os_keypairs_keypair_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypair_name** | **str**| The keypair name.  | 
 **user_id** | **str**| This allows administrative users to operate key-pairs of specified user ID.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_keypairs_keypair_name_get**
> v21_os_keypairs_keypair_name_get(keypair_name, user_id=user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsKeypairsApi()
keypair_name = 'keypair_name_example' # str | The keypair name. 
user_id = 'user_id_example' # str | This allows administrative users to operate key-pairs of specified user ID.  (optional)

try:
    api_instance.v21_os_keypairs_keypair_name_get(keypair_name, user_id=user_id)
except ApiException as e:
    print("Exception when calling OsKeypairsApi->v21_os_keypairs_keypair_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypair_name** | **str**| The keypair name.  | 
 **user_id** | **str**| This allows administrative users to operate key-pairs of specified user ID.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_keypairs_post**
> v21_os_keypairs_post(keypairs_import_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsKeypairsApi()
keypairs_import_post_req = swagger_client.KeypairsImportPostReq() # KeypairsImportPostReq | 

try:
    api_instance.v21_os_keypairs_post(keypairs_import_post_req)
except ApiException as e:
    print("Exception when calling OsKeypairsApi->v21_os_keypairs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypairs_import_post_req** | [**KeypairsImportPostReq**](KeypairsImportPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


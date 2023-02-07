# swagger_client.OsQuotaClassSetsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_quota_class_sets_id_get**](OsQuotaClassSetsApi.md#v21_os_quota_class_sets_id_get) | **GET** /v2.1/os-quota-class-sets/{id} | 
[**v21_os_quota_class_sets_id_put**](OsQuotaClassSetsApi.md#v21_os_quota_class_sets_id_put) | **PUT** /v2.1/os-quota-class-sets/{id} | 


# **v21_os_quota_class_sets_id_get**
> v21_os_quota_class_sets_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsQuotaClassSetsApi()
id = 'id_example' # str | The ID of the quota class. Nova supports the ``default`` Quota Class only. 

try:
    api_instance.v21_os_quota_class_sets_id_get(id)
except ApiException as e:
    print("Exception when calling OsQuotaClassSetsApi->v21_os_quota_class_sets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the quota class. Nova supports the &#x60;&#x60;default&#x60;&#x60; Quota Class only.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_quota_class_sets_id_put**
> v21_os_quota_class_sets_id_put(id, quota_classes_update_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsQuotaClassSetsApi()
id = 'id_example' # str | The ID of the quota class. Nova supports the ``default`` Quota Class only. 
quota_classes_update_post_req = swagger_client.QuotaClassesUpdatePostReq() # QuotaClassesUpdatePostReq | 

try:
    api_instance.v21_os_quota_class_sets_id_put(id, quota_classes_update_post_req)
except ApiException as e:
    print("Exception when calling OsQuotaClassSetsApi->v21_os_quota_class_sets_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the quota class. Nova supports the &#x60;&#x60;default&#x60;&#x60; Quota Class only.  | 
 **quota_classes_update_post_req** | [**QuotaClassesUpdatePostReq**](QuotaClassesUpdatePostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


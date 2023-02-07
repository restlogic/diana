# swagger_client.OsFpingApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_fping_get**](OsFpingApi.md#v21_os_fping_get) | **GET** /v2.1/os-fping | 
[**v21_os_fping_instance_id_get**](OsFpingApi.md#v21_os_fping_instance_id_get) | **GET** /v2.1/os-fping/{instance_id} | 


# **v21_os_fping_get**
> v21_os_fping_get(all_tenants=all_tenants, include=include, exclude=exclude)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFpingApi()
all_tenants = 'all_tenants_example' # str | Specify the ``all_tenants`` query parameter to ping instances for all tenants. By default this is only allowed by admin users. Value of this query parameter is not checked, only presence is considered as request for all tenants.  (optional)
include = 'include_example' # str | Specify ``include=uuid[,uuid...]`` to include the instances in the results.  (optional)
exclude = 'exclude_example' # str | Specify ``exclude=uuid[,uuid...]`` to exclude the instances from the results.  (optional)

try:
    api_instance.v21_os_fping_get(all_tenants=all_tenants, include=include, exclude=exclude)
except ApiException as e:
    print("Exception when calling OsFpingApi->v21_os_fping_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_tenants** | **str**| Specify the &#x60;&#x60;all_tenants&#x60;&#x60; query parameter to ping instances for all tenants. By default this is only allowed by admin users. Value of this query parameter is not checked, only presence is considered as request for all tenants.  | [optional] 
 **include** | **str**| Specify &#x60;&#x60;include&#x3D;uuid[,uuid...]&#x60;&#x60; to include the instances in the results.  | [optional] 
 **exclude** | **str**| Specify &#x60;&#x60;exclude&#x3D;uuid[,uuid...]&#x60;&#x60; to exclude the instances from the results.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_fping_instance_id_get**
> v21_os_fping_instance_id_get(instance_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFpingApi()
instance_id = 'instance_id_example' # str | The UUID of the instance. 

try:
    api_instance.v21_os_fping_instance_id_get(instance_id)
except ApiException as e:
    print("Exception when calling OsFpingApi->v21_os_fping_instance_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The UUID of the instance.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.LimitsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_limits_get**](LimitsApi.md#v21_limits_get) | **GET** /v2.1/limits | 


# **v21_limits_get**
> v21_limits_get(reserved=reserved, tenant_id=tenant_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LimitsApi()
reserved = 56 # int | Specify whether the result of resource total includes reserved resources or not.    - ``0``: Not include reserved resources.   - Other than 0: Include reserved resources.  If non integer value is specified, it is the same as ``0``.  (optional)
tenant_id = 'tenant_id_example' # str | Specify the project ID (tenant ID) to show the rate and absolute limits. This parameter can be specified by admin only.  (optional)

try:
    api_instance.v21_limits_get(reserved=reserved, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling LimitsApi->v21_limits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserved** | **int**| Specify whether the result of resource total includes reserved resources or not.    - &#x60;&#x60;0&#x60;&#x60;: Not include reserved resources.   - Other than 0: Include reserved resources.  If non integer value is specified, it is the same as &#x60;&#x60;0&#x60;&#x60;.  | [optional] 
 **tenant_id** | **str**| Specify the project ID (tenant ID) to show the rate and absolute limits. This parameter can be specified by admin only.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


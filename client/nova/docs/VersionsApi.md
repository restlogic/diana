# swagger_client.VersionsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_api_version_get**](VersionsApi.md#v21_api_version_get) | **GET** /v2.1/{api_version}/ | 
[**v21_get**](VersionsApi.md#v21_get) | **GET** /v2.1/ | 


# **v21_api_version_get**
> v21_api_version_get(api_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
api_version = 'api_version_example' # str | The API version as returned in the links from the ``GET /`` call. 

try:
    api_instance.v21_api_version_get(api_version)
except ApiException as e:
    print("Exception when calling VersionsApi->v21_api_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The API version as returned in the links from the &#x60;&#x60;GET /&#x60;&#x60; call.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_get**
> v21_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()

try:
    api_instance.v21_get()
except ApiException as e:
    print("Exception when calling VersionsApi->v21_get: %s\n" % e)
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


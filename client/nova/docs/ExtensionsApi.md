# swagger_client.ExtensionsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_extensions_alias_get**](ExtensionsApi.md#v21_extensions_alias_get) | **GET** /v2.1/extensions/{alias} | 
[**v21_extensions_get**](ExtensionsApi.md#v21_extensions_get) | **GET** /v2.1/extensions | 


# **v21_extensions_alias_get**
> v21_extensions_alias_get(alias)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()
alias = 'alias_example' # str | A short name by which this extension is also known. 

try:
    api_instance.v21_extensions_alias_get(alias)
except ApiException as e:
    print("Exception when calling ExtensionsApi->v21_extensions_alias_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| A short name by which this extension is also known.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_extensions_get**
> v21_extensions_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()

try:
    api_instance.v21_extensions_get()
except ApiException as e:
    print("Exception when calling ExtensionsApi->v21_extensions_get: %s\n" % e)
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


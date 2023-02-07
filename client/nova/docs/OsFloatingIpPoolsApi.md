# swagger_client.OsFloatingIpPoolsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_floating_ip_pools_get**](OsFloatingIpPoolsApi.md#v21_os_floating_ip_pools_get) | **GET** /v2.1/os-floating-ip-pools | 


# **v21_os_floating_ip_pools_get**
> v21_os_floating_ip_pools_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpPoolsApi()

try:
    api_instance.v21_os_floating_ip_pools_get()
except ApiException as e:
    print("Exception when calling OsFloatingIpPoolsApi->v21_os_floating_ip_pools_get: %s\n" % e)
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


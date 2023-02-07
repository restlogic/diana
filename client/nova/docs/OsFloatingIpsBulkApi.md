# swagger_client.OsFloatingIpsBulkApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_floating_ips_bulk_delete_put**](OsFloatingIpsBulkApi.md#v21_os_floating_ips_bulk_delete_put) | **PUT** /v2.1/os-floating-ips-bulk/delete | 
[**v21_os_floating_ips_bulk_get**](OsFloatingIpsBulkApi.md#v21_os_floating_ips_bulk_get) | **GET** /v2.1/os-floating-ips-bulk | 
[**v21_os_floating_ips_bulk_host_name_get**](OsFloatingIpsBulkApi.md#v21_os_floating_ips_bulk_host_name_get) | **GET** /v2.1/os-floating-ips-bulk/{host_name} | 
[**v21_os_floating_ips_bulk_post**](OsFloatingIpsBulkApi.md#v21_os_floating_ips_bulk_post) | **POST** /v2.1/os-floating-ips-bulk | 


# **v21_os_floating_ips_bulk_delete_put**
> v21_os_floating_ips_bulk_delete_put(floating_ips_bulk_delete_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsBulkApi()
floating_ips_bulk_delete_req = swagger_client.FloatingIpsBulkDeleteReq() # FloatingIpsBulkDeleteReq | 

try:
    api_instance.v21_os_floating_ips_bulk_delete_put(floating_ips_bulk_delete_req)
except ApiException as e:
    print("Exception when calling OsFloatingIpsBulkApi->v21_os_floating_ips_bulk_delete_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ips_bulk_delete_req** | [**FloatingIpsBulkDeleteReq**](FloatingIpsBulkDeleteReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_floating_ips_bulk_get**
> v21_os_floating_ips_bulk_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsBulkApi()

try:
    api_instance.v21_os_floating_ips_bulk_get()
except ApiException as e:
    print("Exception when calling OsFloatingIpsBulkApi->v21_os_floating_ips_bulk_get: %s\n" % e)
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

# **v21_os_floating_ips_bulk_host_name_get**
> v21_os_floating_ips_bulk_host_name_get(host_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsBulkApi()
host_name = 'host_name_example' # str | The name of the host. 

try:
    api_instance.v21_os_floating_ips_bulk_host_name_get(host_name)
except ApiException as e:
    print("Exception when calling OsFloatingIpsBulkApi->v21_os_floating_ips_bulk_host_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| The name of the host.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_floating_ips_bulk_post**
> v21_os_floating_ips_bulk_post(floating_ips_bulk_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsBulkApi()
floating_ips_bulk_create_req = swagger_client.FloatingIpsBulkCreateReq() # FloatingIpsBulkCreateReq | 

try:
    api_instance.v21_os_floating_ips_bulk_post(floating_ips_bulk_create_req)
except ApiException as e:
    print("Exception when calling OsFloatingIpsBulkApi->v21_os_floating_ips_bulk_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ips_bulk_create_req** | [**FloatingIpsBulkCreateReq**](FloatingIpsBulkCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


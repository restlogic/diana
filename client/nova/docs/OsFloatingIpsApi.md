# swagger_client.OsFloatingIpsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_floating_ips_floating_ip_id_delete**](OsFloatingIpsApi.md#v21_os_floating_ips_floating_ip_id_delete) | **DELETE** /v2.1/os-floating-ips/{floating_ip_id} | 
[**v21_os_floating_ips_floating_ip_id_get**](OsFloatingIpsApi.md#v21_os_floating_ips_floating_ip_id_get) | **GET** /v2.1/os-floating-ips/{floating_ip_id} | 
[**v21_os_floating_ips_get**](OsFloatingIpsApi.md#v21_os_floating_ips_get) | **GET** /v2.1/os-floating-ips | 
[**v21_os_floating_ips_post**](OsFloatingIpsApi.md#v21_os_floating_ips_post) | **POST** /v2.1/os-floating-ips | 


# **v21_os_floating_ips_floating_ip_id_delete**
> v21_os_floating_ips_floating_ip_id_delete(floating_ip_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsApi()
floating_ip_id = 'floating_ip_id_example' # str | The ID of the floating IP address. 

try:
    api_instance.v21_os_floating_ips_floating_ip_id_delete(floating_ip_id)
except ApiException as e:
    print("Exception when calling OsFloatingIpsApi->v21_os_floating_ips_floating_ip_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | **str**| The ID of the floating IP address.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_floating_ips_floating_ip_id_get**
> v21_os_floating_ips_floating_ip_id_get(floating_ip_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsApi()
floating_ip_id = 'floating_ip_id_example' # str | The ID of the floating IP address. 

try:
    api_instance.v21_os_floating_ips_floating_ip_id_get(floating_ip_id)
except ApiException as e:
    print("Exception when calling OsFloatingIpsApi->v21_os_floating_ips_floating_ip_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | **str**| The ID of the floating IP address.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_floating_ips_get**
> v21_os_floating_ips_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsApi()

try:
    api_instance.v21_os_floating_ips_get()
except ApiException as e:
    print("Exception when calling OsFloatingIpsApi->v21_os_floating_ips_get: %s\n" % e)
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

# **v21_os_floating_ips_post**
> v21_os_floating_ips_post(floating_ips_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFloatingIpsApi()
floating_ips_create_req = swagger_client.FloatingIpsCreateReq() # FloatingIpsCreateReq | 

try:
    api_instance.v21_os_floating_ips_post(floating_ips_create_req)
except ApiException as e:
    print("Exception when calling OsFloatingIpsApi->v21_os_floating_ips_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ips_create_req** | [**FloatingIpsCreateReq**](FloatingIpsCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


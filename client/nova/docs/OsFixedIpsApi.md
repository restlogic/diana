# swagger_client.OsFixedIpsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_fixed_ips_fixed_ip_action_post**](OsFixedIpsApi.md#v21_os_fixed_ips_fixed_ip_action_post) | **POST** /v2.1/os-fixed-ips/{fixed_ip}/action | 
[**v21_os_fixed_ips_fixed_ip_get**](OsFixedIpsApi.md#v21_os_fixed_ips_fixed_ip_get) | **GET** /v2.1/os-fixed-ips/{fixed_ip} | 


# **v21_os_fixed_ips_fixed_ip_action_post**
> v21_os_fixed_ips_fixed_ip_action_post(fixed_ip, fixedip_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFixedIpsApi()
fixed_ip = 'fixed_ip_example' # str | The fixed IP of interest to you. 
fixedip_post_req = swagger_client.FixedipPostReq() # FixedipPostReq | 

try:
    api_instance.v21_os_fixed_ips_fixed_ip_action_post(fixed_ip, fixedip_post_req)
except ApiException as e:
    print("Exception when calling OsFixedIpsApi->v21_os_fixed_ips_fixed_ip_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_ip** | **str**| The fixed IP of interest to you.  | 
 **fixedip_post_req** | [**FixedipPostReq**](FixedipPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_fixed_ips_fixed_ip_get**
> v21_os_fixed_ips_fixed_ip_get(fixed_ip)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFixedIpsApi()
fixed_ip = 'fixed_ip_example' # str | The fixed IP of interest to you. 

try:
    api_instance.v21_os_fixed_ips_fixed_ip_get(fixed_ip)
except ApiException as e:
    print("Exception when calling OsFixedIpsApi->v21_os_fixed_ips_fixed_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_ip** | **str**| The fixed IP of interest to you.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


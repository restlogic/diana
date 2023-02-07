# swagger_client.OsHostsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_hosts_get**](OsHostsApi.md#v21_os_hosts_get) | **GET** /v2.1/os-hosts | 
[**v21_os_hosts_host_name_get**](OsHostsApi.md#v21_os_hosts_host_name_get) | **GET** /v2.1/os-hosts/{host_name} | 
[**v21_os_hosts_host_name_put**](OsHostsApi.md#v21_os_hosts_host_name_put) | **PUT** /v2.1/os-hosts/{host_name} | 
[**v21_os_hosts_host_name_reboot_get**](OsHostsApi.md#v21_os_hosts_host_name_reboot_get) | **GET** /v2.1/os-hosts/{host_name}/reboot | 
[**v21_os_hosts_host_name_shutdown_get**](OsHostsApi.md#v21_os_hosts_host_name_shutdown_get) | **GET** /v2.1/os-hosts/{host_name}/shutdown | 
[**v21_os_hosts_host_name_startup_get**](OsHostsApi.md#v21_os_hosts_host_name_startup_get) | **GET** /v2.1/os-hosts/{host_name}/startup | 


# **v21_os_hosts_get**
> v21_os_hosts_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()

try:
    api_instance.v21_os_hosts_get()
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_get: %s\n" % e)
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

# **v21_os_hosts_host_name_get**
> v21_os_hosts_host_name_get(host_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()
host_name = 'host_name_example' # str | The name of the host. 

try:
    api_instance.v21_os_hosts_host_name_get(host_name)
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_host_name_get: %s\n" % e)
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

# **v21_os_hosts_host_name_put**
> v21_os_hosts_host_name_put(host_name, host_put_maintenance_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()
host_name = 'host_name_example' # str | The name of the host. 
host_put_maintenance_req = swagger_client.HostPutMaintenanceReq() # HostPutMaintenanceReq | 

try:
    api_instance.v21_os_hosts_host_name_put(host_name, host_put_maintenance_req)
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_host_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| The name of the host.  | 
 **host_put_maintenance_req** | [**HostPutMaintenanceReq**](HostPutMaintenanceReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_hosts_host_name_reboot_get**
> v21_os_hosts_host_name_reboot_get(host_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()
host_name = 'host_name_example' # str | The name of the host. 

try:
    api_instance.v21_os_hosts_host_name_reboot_get(host_name)
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_host_name_reboot_get: %s\n" % e)
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

# **v21_os_hosts_host_name_shutdown_get**
> v21_os_hosts_host_name_shutdown_get(host_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()
host_name = 'host_name_example' # str | The name of the host. 

try:
    api_instance.v21_os_hosts_host_name_shutdown_get(host_name)
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_host_name_shutdown_get: %s\n" % e)
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

# **v21_os_hosts_host_name_startup_get**
> v21_os_hosts_host_name_startup_get(host_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsHostsApi()
host_name = 'host_name_example' # str | The name of the host. 

try:
    api_instance.v21_os_hosts_host_name_startup_get(host_name)
except ApiException as e:
    print("Exception when calling OsHostsApi->v21_os_hosts_host_name_startup_get: %s\n" % e)
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


# swagger_client.OsTenantNetworkApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_tenant_networks_get**](OsTenantNetworkApi.md#v21_os_tenant_networks_get) | **GET** /v2.1/os-tenant-networks | 
[**v21_os_tenant_networks_network_id_delete**](OsTenantNetworkApi.md#v21_os_tenant_networks_network_id_delete) | **DELETE** /v2.1/os-tenant-networks/{network_id} | 
[**v21_os_tenant_networks_network_id_get**](OsTenantNetworkApi.md#v21_os_tenant_networks_network_id_get) | **GET** /v2.1/os-tenant-networks/{network_id} | 
[**v21_os_tenant_networks_post**](OsTenantNetworkApi.md#v21_os_tenant_networks_post) | **POST** /v2.1/os-tenant-networks | 


# **v21_os_tenant_networks_get**
> v21_os_tenant_networks_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsTenantNetworkApi()

try:
    api_instance.v21_os_tenant_networks_get()
except ApiException as e:
    print("Exception when calling OsTenantNetworkApi->v21_os_tenant_networks_get: %s\n" % e)
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

# **v21_os_tenant_networks_network_id_delete**
> v21_os_tenant_networks_network_id_delete(network_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsTenantNetworkApi()
network_id = 'network_id_example' # str | The UUID of the network. 

try:
    api_instance.v21_os_tenant_networks_network_id_delete(network_id)
except ApiException as e:
    print("Exception when calling OsTenantNetworkApi->v21_os_tenant_networks_network_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The UUID of the network.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_tenant_networks_network_id_get**
> v21_os_tenant_networks_network_id_get(network_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsTenantNetworkApi()
network_id = 'network_id_example' # str | The UUID of the network. 

try:
    api_instance.v21_os_tenant_networks_network_id_get(network_id)
except ApiException as e:
    print("Exception when calling OsTenantNetworkApi->v21_os_tenant_networks_network_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The UUID of the network.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_tenant_networks_post**
> v21_os_tenant_networks_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsTenantNetworkApi()

try:
    api_instance.v21_os_tenant_networks_post()
except ApiException as e:
    print("Exception when calling OsTenantNetworkApi->v21_os_tenant_networks_post: %s\n" % e)
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


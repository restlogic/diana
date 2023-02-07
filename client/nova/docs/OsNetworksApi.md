# swagger_client.OsNetworksApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_networks_add_post**](OsNetworksApi.md#v21_os_networks_add_post) | **POST** /v2.1/os-networks/add | 
[**v21_os_networks_get**](OsNetworksApi.md#v21_os_networks_get) | **GET** /v2.1/os-networks | 
[**v21_os_networks_network_id_action_post**](OsNetworksApi.md#v21_os_networks_network_id_action_post) | **POST** /v2.1/os-networks/{network_id}/action | 
[**v21_os_networks_network_id_delete**](OsNetworksApi.md#v21_os_networks_network_id_delete) | **DELETE** /v2.1/os-networks/{network_id} | 
[**v21_os_networks_network_id_get**](OsNetworksApi.md#v21_os_networks_network_id_get) | **GET** /v2.1/os-networks/{network_id} | 
[**v21_os_networks_post**](OsNetworksApi.md#v21_os_networks_post) | **POST** /v2.1/os-networks | 


# **v21_os_networks_add_post**
> v21_os_networks_add_post(network_add_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()
network_add_req = swagger_client.NetworkAddReq() # NetworkAddReq | 

try:
    api_instance.v21_os_networks_add_post(network_add_req)
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_add_req** | [**NetworkAddReq**](NetworkAddReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_networks_get**
> v21_os_networks_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()

try:
    api_instance.v21_os_networks_get()
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_get: %s\n" % e)
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

# **v21_os_networks_network_id_action_post**
> v21_os_networks_network_id_action_post(network_id, network_associate_host_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()
network_id = 'network_id_example' # str | The UUID of the network. 
network_associate_host_req = swagger_client.NetworkAssociateHostReq() # NetworkAssociateHostReq | 

try:
    api_instance.v21_os_networks_network_id_action_post(network_id, network_associate_host_req)
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_network_id_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The UUID of the network.  | 
 **network_associate_host_req** | [**NetworkAssociateHostReq**](NetworkAssociateHostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_networks_network_id_delete**
> v21_os_networks_network_id_delete(network_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()
network_id = 'network_id_example' # str | The UUID of the network. 

try:
    api_instance.v21_os_networks_network_id_delete(network_id)
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_network_id_delete: %s\n" % e)
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

# **v21_os_networks_network_id_get**
> v21_os_networks_network_id_get(network_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()
network_id = 'network_id_example' # str | The UUID of the network. 

try:
    api_instance.v21_os_networks_network_id_get(network_id)
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_network_id_get: %s\n" % e)
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

# **v21_os_networks_post**
> v21_os_networks_post(network_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsNetworksApi()
network_create_req = swagger_client.NetworkCreateReq() # NetworkCreateReq | 

try:
    api_instance.v21_os_networks_post(network_create_req)
except ApiException as e:
    print("Exception when calling OsNetworksApi->v21_os_networks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_create_req** | [**NetworkCreateReq**](NetworkCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


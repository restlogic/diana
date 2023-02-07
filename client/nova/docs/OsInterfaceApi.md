# swagger_client.OsInterfaceApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_os_interface_get**](OsInterfaceApi.md#v21_servers_server_id_os_interface_get) | **GET** /v2.1/servers/{server_id}/os-interface | 
[**v21_servers_server_id_os_interface_port_id_delete**](OsInterfaceApi.md#v21_servers_server_id_os_interface_port_id_delete) | **DELETE** /v2.1/servers/{server_id}/os-interface/{port_id} | 
[**v21_servers_server_id_os_interface_port_id_get**](OsInterfaceApi.md#v21_servers_server_id_os_interface_port_id_get) | **GET** /v2.1/servers/{server_id}/os-interface/{port_id} | 
[**v21_servers_server_id_os_interface_post**](OsInterfaceApi.md#v21_servers_server_id_os_interface_post) | **POST** /v2.1/servers/{server_id}/os-interface | 


# **v21_servers_server_id_os_interface_get**
> v21_servers_server_id_os_interface_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInterfaceApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_os_interface_get(server_id)
except ApiException as e:
    print("Exception when calling OsInterfaceApi->v21_servers_server_id_os_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_interface_port_id_delete**
> v21_servers_server_id_os_interface_port_id_delete(server_id, port_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInterfaceApi()
server_id = 'server_id_example' # str | The UUID of the server. 
port_id = 'port_id_example' # str | The UUID of the port. 

try:
    api_instance.v21_servers_server_id_os_interface_port_id_delete(server_id, port_id)
except ApiException as e:
    print("Exception when calling OsInterfaceApi->v21_servers_server_id_os_interface_port_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **port_id** | **str**| The UUID of the port.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_interface_port_id_get**
> v21_servers_server_id_os_interface_port_id_get(server_id, port_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInterfaceApi()
server_id = 'server_id_example' # str | The UUID of the server. 
port_id = 'port_id_example' # str | The UUID of the port. 

try:
    api_instance.v21_servers_server_id_os_interface_port_id_get(server_id, port_id)
except ApiException as e:
    print("Exception when calling OsInterfaceApi->v21_servers_server_id_os_interface_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **port_id** | **str**| The UUID of the port.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_interface_post**
> v21_servers_server_id_os_interface_post(server_id, attach_interfaces_create_net_id_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInterfaceApi()
server_id = 'server_id_example' # str | The UUID of the server. 
attach_interfaces_create_net_id_req = swagger_client.AttachInterfacesCreateNetIdReq() # AttachInterfacesCreateNetIdReq | 

try:
    api_instance.v21_servers_server_id_os_interface_post(server_id, attach_interfaces_create_net_id_req)
except ApiException as e:
    print("Exception when calling OsInterfaceApi->v21_servers_server_id_os_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **attach_interfaces_create_net_id_req** | [**AttachInterfacesCreateNetIdReq**](AttachInterfacesCreateNetIdReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


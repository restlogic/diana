# swagger_client.OsBaremetalNodesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_baremetal_nodes_get**](OsBaremetalNodesApi.md#v21_os_baremetal_nodes_get) | **GET** /v2.1/os-baremetal-nodes | 
[**v21_os_baremetal_nodes_node_id_get**](OsBaremetalNodesApi.md#v21_os_baremetal_nodes_node_id_get) | **GET** /v2.1/os-baremetal-nodes/{node_id} | 


# **v21_os_baremetal_nodes_get**
> v21_os_baremetal_nodes_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsBaremetalNodesApi()

try:
    api_instance.v21_os_baremetal_nodes_get()
except ApiException as e:
    print("Exception when calling OsBaremetalNodesApi->v21_os_baremetal_nodes_get: %s\n" % e)
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

# **v21_os_baremetal_nodes_node_id_get**
> v21_os_baremetal_nodes_node_id_get(node_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsBaremetalNodesApi()
node_id = 'node_id_example' # str | The node ID. 

try:
    api_instance.v21_os_baremetal_nodes_node_id_get(node_id)
except ApiException as e:
    print("Exception when calling OsBaremetalNodesApi->v21_os_baremetal_nodes_node_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The node ID.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


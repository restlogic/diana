# swagger_client.OsCellsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_cells_capacities_get**](OsCellsApi.md#v21_os_cells_capacities_get) | **GET** /v2.1/os-cells/capacities | 
[**v21_os_cells_cell_id_capacities_get**](OsCellsApi.md#v21_os_cells_cell_id_capacities_get) | **GET** /v2.1/os-cells/{cell_id}/capacities | 
[**v21_os_cells_cell_id_delete**](OsCellsApi.md#v21_os_cells_cell_id_delete) | **DELETE** /v2.1/os-cells/{cell_id} | 
[**v21_os_cells_cell_id_get**](OsCellsApi.md#v21_os_cells_cell_id_get) | **GET** /v2.1/os-cells/{cell_id} | 
[**v21_os_cells_cell_id_put**](OsCellsApi.md#v21_os_cells_cell_id_put) | **PUT** /v2.1/os-cells/{cell_id} | 
[**v21_os_cells_detail_get**](OsCellsApi.md#v21_os_cells_detail_get) | **GET** /v2.1/os-cells/detail | 
[**v21_os_cells_get**](OsCellsApi.md#v21_os_cells_get) | **GET** /v2.1/os-cells | 
[**v21_os_cells_info_get**](OsCellsApi.md#v21_os_cells_info_get) | **GET** /v2.1/os-cells/info | 
[**v21_os_cells_post**](OsCellsApi.md#v21_os_cells_post) | **POST** /v2.1/os-cells | 


# **v21_os_cells_capacities_get**
> v21_os_cells_capacities_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()

try:
    api_instance.v21_os_cells_capacities_get()
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_capacities_get: %s\n" % e)
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

# **v21_os_cells_cell_id_capacities_get**
> v21_os_cells_cell_id_capacities_get(cell_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()
cell_id = 'cell_id_example' # str | The UUID of the cell. 

try:
    api_instance.v21_os_cells_cell_id_capacities_get(cell_id)
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_cell_id_capacities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | **str**| The UUID of the cell.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_cells_cell_id_delete**
> v21_os_cells_cell_id_delete()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()

try:
    api_instance.v21_os_cells_cell_id_delete()
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_cell_id_delete: %s\n" % e)
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

# **v21_os_cells_cell_id_get**
> v21_os_cells_cell_id_get(cell_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()
cell_id = 'cell_id_example' # str | The UUID of the cell. 

try:
    api_instance.v21_os_cells_cell_id_get(cell_id)
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_cell_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | **str**| The UUID of the cell.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_cells_cell_id_put**
> v21_os_cells_cell_id_put()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()

try:
    api_instance.v21_os_cells_cell_id_put()
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_cell_id_put: %s\n" % e)
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

# **v21_os_cells_detail_get**
> v21_os_cells_detail_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_cells_detail_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Used in conjunction with &#x60;&#x60;offset&#x60;&#x60; to return a slice of items. &#x60;&#x60;limit&#x60;&#x60; is the maximum number of items to return. If &#x60;&#x60;limit&#x60;&#x60; is not specified, or exceeds the configurable &#x60;&#x60;max_limit&#x60;&#x60;, then &#x60;&#x60;max_limit&#x60;&#x60; will be used instead.  | [optional] 
 **offset** | **int**| Used in conjunction with &#x60;&#x60;limit&#x60;&#x60; to return a slice of items. &#x60;&#x60;offset&#x60;&#x60; is where to start in the list.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_cells_get**
> v21_os_cells_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_cells_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Used in conjunction with &#x60;&#x60;offset&#x60;&#x60; to return a slice of items. &#x60;&#x60;limit&#x60;&#x60; is the maximum number of items to return. If &#x60;&#x60;limit&#x60;&#x60; is not specified, or exceeds the configurable &#x60;&#x60;max_limit&#x60;&#x60;, then &#x60;&#x60;max_limit&#x60;&#x60; will be used instead.  | [optional] 
 **offset** | **int**| Used in conjunction with &#x60;&#x60;limit&#x60;&#x60; to return a slice of items. &#x60;&#x60;offset&#x60;&#x60; is where to start in the list.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_cells_info_get**
> v21_os_cells_info_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()

try:
    api_instance.v21_os_cells_info_get()
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_info_get: %s\n" % e)
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

# **v21_os_cells_post**
> v21_os_cells_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCellsApi()

try:
    api_instance.v21_os_cells_post()
except ApiException as e:
    print("Exception when calling OsCellsApi->v21_os_cells_post: %s\n" % e)
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


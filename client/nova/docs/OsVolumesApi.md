# swagger_client.OsVolumesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_snapshots_detail_get**](OsVolumesApi.md#v21_os_snapshots_detail_get) | **GET** /v2.1/os-snapshots/detail | 
[**v21_os_snapshots_get**](OsVolumesApi.md#v21_os_snapshots_get) | **GET** /v2.1/os-snapshots | 
[**v21_os_snapshots_post**](OsVolumesApi.md#v21_os_snapshots_post) | **POST** /v2.1/os-snapshots | 
[**v21_os_snapshots_snapshot_id_delete**](OsVolumesApi.md#v21_os_snapshots_snapshot_id_delete) | **DELETE** /v2.1/os-snapshots/{snapshot_id} | 
[**v21_os_snapshots_snapshot_id_get**](OsVolumesApi.md#v21_os_snapshots_snapshot_id_get) | **GET** /v2.1/os-snapshots/{snapshot_id} | 
[**v21_os_volumes_detail_get**](OsVolumesApi.md#v21_os_volumes_detail_get) | **GET** /v2.1/os-volumes/detail | 
[**v21_os_volumes_get**](OsVolumesApi.md#v21_os_volumes_get) | **GET** /v2.1/os-volumes | 
[**v21_os_volumes_post**](OsVolumesApi.md#v21_os_volumes_post) | **POST** /v2.1/os-volumes | 
[**v21_os_volumes_volume_id_delete**](OsVolumesApi.md#v21_os_volumes_volume_id_delete) | **DELETE** /v2.1/os-volumes/{volume_id} | 
[**v21_os_volumes_volume_id_get**](OsVolumesApi.md#v21_os_volumes_volume_id_get) | **GET** /v2.1/os-volumes/{volume_id} | 


# **v21_os_snapshots_detail_get**
> v21_os_snapshots_detail_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_snapshots_detail_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_snapshots_detail_get: %s\n" % e)
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

# **v21_os_snapshots_get**
> v21_os_snapshots_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_snapshots_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_snapshots_get: %s\n" % e)
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

# **v21_os_snapshots_post**
> v21_os_snapshots_post(snapshot_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
snapshot_create_req = swagger_client.SnapshotCreateReq() # SnapshotCreateReq | 

try:
    api_instance.v21_os_snapshots_post(snapshot_create_req)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_create_req** | [**SnapshotCreateReq**](SnapshotCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_snapshots_snapshot_id_delete**
> v21_os_snapshots_snapshot_id_delete(snapshot_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
snapshot_id = 'snapshot_id_example' # str | The UUID of the snapshot. 

try:
    api_instance.v21_os_snapshots_snapshot_id_delete(snapshot_id)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_snapshots_snapshot_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The UUID of the snapshot.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_snapshots_snapshot_id_get**
> v21_os_snapshots_snapshot_id_get(snapshot_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
snapshot_id = 'snapshot_id_example' # str | The UUID of the snapshot. 

try:
    api_instance.v21_os_snapshots_snapshot_id_get(snapshot_id)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_snapshots_snapshot_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The UUID of the snapshot.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_volumes_detail_get**
> v21_os_volumes_detail_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_volumes_detail_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_volumes_detail_get: %s\n" % e)
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

# **v21_os_volumes_get**
> v21_os_volumes_get(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_volumes_get(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_volumes_get: %s\n" % e)
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

# **v21_os_volumes_post**
> v21_os_volumes_post(os_volumes_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
os_volumes_post_req = swagger_client.OsVolumesPostReq() # OsVolumesPostReq | 

try:
    api_instance.v21_os_volumes_post(os_volumes_post_req)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_volumes_post_req** | [**OsVolumesPostReq**](OsVolumesPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_volumes_volume_id_delete**
> v21_os_volumes_volume_id_delete(volume_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
volume_id = 'volume_id_example' # str | The unique ID for a volume. 

try:
    api_instance.v21_os_volumes_volume_id_delete(volume_id)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_volumes_volume_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The unique ID for a volume.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_volumes_volume_id_get**
> v21_os_volumes_volume_id_get(volume_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumesApi()
volume_id = 'volume_id_example' # str | The unique ID for a volume. 

try:
    api_instance.v21_os_volumes_volume_id_get(volume_id)
except ApiException as e:
    print("Exception when calling OsVolumesApi->v21_os_volumes_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The unique ID for a volume.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


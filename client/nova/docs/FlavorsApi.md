# swagger_client.FlavorsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_flavors_detail_get**](FlavorsApi.md#v21_flavors_detail_get) | **GET** /v2.1/flavors/detail | 
[**v21_flavors_flavor_id_delete**](FlavorsApi.md#v21_flavors_flavor_id_delete) | **DELETE** /v2.1/flavors/{flavor_id} | 
[**v21_flavors_flavor_id_get**](FlavorsApi.md#v21_flavors_flavor_id_get) | **GET** /v2.1/flavors/{flavor_id} | 
[**v21_flavors_flavor_id_put**](FlavorsApi.md#v21_flavors_flavor_id_put) | **PUT** /v2.1/flavors/{flavor_id} | 
[**v21_flavors_get**](FlavorsApi.md#v21_flavors_get) | **GET** /v2.1/flavors | 
[**v21_flavors_post**](FlavorsApi.md#v21_flavors_post) | **POST** /v2.1/flavors | 


# **v21_flavors_detail_get**
> v21_flavors_detail_get(sort_key=sort_key, sort_dir=sort_dir, limit=limit, marker=marker, min_disk=min_disk, min_ram=min_ram, is_public=is_public)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
sort_key = 'sort_key_example' # str | Sorts by a flavor attribute. Default attribute is ``flavorid``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor ``sort_key`` attribute. The sort keys are limited to:  - ``created_at`` - ``description`` - ``disabled`` - ``ephemeral_gb`` - ``flavorid`` - ``id`` - ``is_public`` - ``memory_mb`` - ``name`` - ``root_gb`` - ``rxtx_factor`` - ``swap`` - ``updated_at`` - ``vcpu_weight`` - ``vcpus``  (optional)
sort_dir = 'sort_dir_example' # str | Sort direction. A valid value is ``asc`` (ascending) or ``desc`` (descending). Default is ``asc``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor ``sort_key`` attribute.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
min_disk = 56 # int | Filters the response by a minimum disk space, in GiB. For example, ``100``.  (optional)
min_ram = 56 # int | Filters the response by a minimum RAM, in MiB. For example, ``512``.  (optional)
is_public = 'is_public_example' # str | This parameter is only applicable to users with the administrative role. For all other non-admin users, the parameter is ignored and only public flavors will be returned. Filters the flavor list based on whether the flavor is public or private. If the value of this parameter is not specified, it is treated as ``True``. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False`` (they are case-insensitive). If the value is ``None`` (case-insensitive) both public and private flavors will be listed in a single request.  (optional)

try:
    api_instance.v21_flavors_detail_get(sort_key=sort_key, sort_dir=sort_dir, limit=limit, marker=marker, min_disk=min_disk, min_ram=min_ram, is_public=is_public)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_key** | **str**| Sorts by a flavor attribute. Default attribute is &#x60;&#x60;flavorid&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor &#x60;&#x60;sort_key&#x60;&#x60; attribute. The sort keys are limited to:  - &#x60;&#x60;created_at&#x60;&#x60; - &#x60;&#x60;description&#x60;&#x60; - &#x60;&#x60;disabled&#x60;&#x60; - &#x60;&#x60;ephemeral_gb&#x60;&#x60; - &#x60;&#x60;flavorid&#x60;&#x60; - &#x60;&#x60;id&#x60;&#x60; - &#x60;&#x60;is_public&#x60;&#x60; - &#x60;&#x60;memory_mb&#x60;&#x60; - &#x60;&#x60;name&#x60;&#x60; - &#x60;&#x60;root_gb&#x60;&#x60; - &#x60;&#x60;rxtx_factor&#x60;&#x60; - &#x60;&#x60;swap&#x60;&#x60; - &#x60;&#x60;updated_at&#x60;&#x60; - &#x60;&#x60;vcpu_weight&#x60;&#x60; - &#x60;&#x60;vcpus&#x60;&#x60;  | [optional] 
 **sort_dir** | **str**| Sort direction. A valid value is &#x60;&#x60;asc&#x60;&#x60; (ascending) or &#x60;&#x60;desc&#x60;&#x60; (descending). Default is &#x60;&#x60;asc&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor &#x60;&#x60;sort_key&#x60;&#x60; attribute.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **min_disk** | **int**| Filters the response by a minimum disk space, in GiB. For example, &#x60;&#x60;100&#x60;&#x60;.  | [optional] 
 **min_ram** | **int**| Filters the response by a minimum RAM, in MiB. For example, &#x60;&#x60;512&#x60;&#x60;.  | [optional] 
 **is_public** | **str**| This parameter is only applicable to users with the administrative role. For all other non-admin users, the parameter is ignored and only public flavors will be returned. Filters the flavor list based on whether the flavor is public or private. If the value of this parameter is not specified, it is treated as &#x60;&#x60;True&#x60;&#x60;. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60; (they are case-insensitive). If the value is &#x60;&#x60;None&#x60;&#x60; (case-insensitive) both public and private flavors will be listed in a single request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_delete**
> v21_flavors_flavor_id_delete(flavor_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 

try:
    api_instance.v21_flavors_flavor_id_delete(flavor_id)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_flavor_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_get**
> v21_flavors_flavor_id_get(flavor_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 

try:
    api_instance.v21_flavors_flavor_id_get(flavor_id)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_flavor_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_put**
> v21_flavors_flavor_id_put(flavor_id, flavor_update_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_update_req = swagger_client.FlavorUpdateReq() # FlavorUpdateReq | 

try:
    api_instance.v21_flavors_flavor_id_put(flavor_id, flavor_update_req)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_flavor_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_update_req** | [**FlavorUpdateReq**](FlavorUpdateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_get**
> v21_flavors_get(sort_key=sort_key, sort_dir=sort_dir, limit=limit, marker=marker, min_disk=min_disk, min_ram=min_ram, is_public=is_public)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
sort_key = 'sort_key_example' # str | Sorts by a flavor attribute. Default attribute is ``flavorid``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor ``sort_key`` attribute. The sort keys are limited to:  - ``created_at`` - ``description`` - ``disabled`` - ``ephemeral_gb`` - ``flavorid`` - ``id`` - ``is_public`` - ``memory_mb`` - ``name`` - ``root_gb`` - ``rxtx_factor`` - ``swap`` - ``updated_at`` - ``vcpu_weight`` - ``vcpus``  (optional)
sort_dir = 'sort_dir_example' # str | Sort direction. A valid value is ``asc`` (ascending) or ``desc`` (descending). Default is ``asc``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor ``sort_key`` attribute.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
min_disk = 56 # int | Filters the response by a minimum disk space, in GiB. For example, ``100``.  (optional)
min_ram = 56 # int | Filters the response by a minimum RAM, in MiB. For example, ``512``.  (optional)
is_public = 'is_public_example' # str | This parameter is only applicable to users with the administrative role. For all other non-admin users, the parameter is ignored and only public flavors will be returned. Filters the flavor list based on whether the flavor is public or private. If the value of this parameter is not specified, it is treated as ``True``. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False`` (they are case-insensitive). If the value is ``None`` (case-insensitive) both public and private flavors will be listed in a single request.  (optional)

try:
    api_instance.v21_flavors_get(sort_key=sort_key, sort_dir=sort_dir, limit=limit, marker=marker, min_disk=min_disk, min_ram=min_ram, is_public=is_public)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_key** | **str**| Sorts by a flavor attribute. Default attribute is &#x60;&#x60;flavorid&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor &#x60;&#x60;sort_key&#x60;&#x60; attribute. The sort keys are limited to:  - &#x60;&#x60;created_at&#x60;&#x60; - &#x60;&#x60;description&#x60;&#x60; - &#x60;&#x60;disabled&#x60;&#x60; - &#x60;&#x60;ephemeral_gb&#x60;&#x60; - &#x60;&#x60;flavorid&#x60;&#x60; - &#x60;&#x60;id&#x60;&#x60; - &#x60;&#x60;is_public&#x60;&#x60; - &#x60;&#x60;memory_mb&#x60;&#x60; - &#x60;&#x60;name&#x60;&#x60; - &#x60;&#x60;root_gb&#x60;&#x60; - &#x60;&#x60;rxtx_factor&#x60;&#x60; - &#x60;&#x60;swap&#x60;&#x60; - &#x60;&#x60;updated_at&#x60;&#x60; - &#x60;&#x60;vcpu_weight&#x60;&#x60; - &#x60;&#x60;vcpus&#x60;&#x60;  | [optional] 
 **sort_dir** | **str**| Sort direction. A valid value is &#x60;&#x60;asc&#x60;&#x60; (ascending) or &#x60;&#x60;desc&#x60;&#x60; (descending). Default is &#x60;&#x60;asc&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the flavor &#x60;&#x60;sort_key&#x60;&#x60; attribute.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **min_disk** | **int**| Filters the response by a minimum disk space, in GiB. For example, &#x60;&#x60;100&#x60;&#x60;.  | [optional] 
 **min_ram** | **int**| Filters the response by a minimum RAM, in MiB. For example, &#x60;&#x60;512&#x60;&#x60;.  | [optional] 
 **is_public** | **str**| This parameter is only applicable to users with the administrative role. For all other non-admin users, the parameter is ignored and only public flavors will be returned. Filters the flavor list based on whether the flavor is public or private. If the value of this parameter is not specified, it is treated as &#x60;&#x60;True&#x60;&#x60;. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60; (they are case-insensitive). If the value is &#x60;&#x60;None&#x60;&#x60; (case-insensitive) both public and private flavors will be listed in a single request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_post**
> v21_flavors_post(flavor_create_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorsApi()
flavor_create_post_req = swagger_client.FlavorCreatePostReq() # FlavorCreatePostReq | 

try:
    api_instance.v21_flavors_post(flavor_create_post_req)
except ApiException as e:
    print("Exception when calling FlavorsApi->v21_flavors_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_create_post_req** | [**FlavorCreatePostReq**](FlavorCreatePostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


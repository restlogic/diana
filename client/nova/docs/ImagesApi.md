# swagger_client.ImagesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_images_detail_get**](ImagesApi.md#v21_images_detail_get) | **GET** /v2.1/images/detail | 
[**v21_images_get**](ImagesApi.md#v21_images_get) | **GET** /v2.1/images | 
[**v21_images_image_id_delete**](ImagesApi.md#v21_images_image_id_delete) | **DELETE** /v2.1/images/{image_id} | 
[**v21_images_image_id_get**](ImagesApi.md#v21_images_image_id_get) | **GET** /v2.1/images/{image_id} | 
[**v21_images_image_id_metadata_get**](ImagesApi.md#v21_images_image_id_metadata_get) | **GET** /v2.1/images/{image_id}/metadata | 
[**v21_images_image_id_metadata_key_delete**](ImagesApi.md#v21_images_image_id_metadata_key_delete) | **DELETE** /v2.1/images/{image_id}/metadata/{key} | 
[**v21_images_image_id_metadata_key_get**](ImagesApi.md#v21_images_image_id_metadata_key_get) | **GET** /v2.1/images/{image_id}/metadata/{key} | 
[**v21_images_image_id_metadata_key_put**](ImagesApi.md#v21_images_image_id_metadata_key_put) | **PUT** /v2.1/images/{image_id}/metadata/{key} | 
[**v21_images_image_id_metadata_post**](ImagesApi.md#v21_images_image_id_metadata_post) | **POST** /v2.1/images/{image_id}/metadata | 
[**v21_images_image_id_metadata_put**](ImagesApi.md#v21_images_image_id_metadata_put) | **PUT** /v2.1/images/{image_id}/metadata | 


# **v21_images_detail_get**
> v21_images_detail_get(changes_since=changes_since, server=server, name=name, status=status, min_disk=min_disk, min_ram=min_ram, type=type, limit=limit, marker=marker)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
changes_since = 'changes_since_example' # str | Filters the response by a date and time when the image last changed status. Use this query parameter to check for changes since a previous request rather than re-downloading and re-parsing the full status at each polling interval. If data has changed, the call returns only the items changed since the ``changes-since`` time. If data has not changed since the ``changes-since`` time, the call returns an empty list. To enable you to keep track of changes, this filter also displays images that were deleted if the ``changes-since`` value specifies a date in the last 30 days. Items deleted more than 30 days ago might be returned, but it is not guaranteed. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_:  ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  (optional)
server = 'server_example' # str | Filters the response by a server, as a URL.  (optional)
name = 'name_example' # str | Filters the response by an image name, as a string.  (optional)
status = 'status_example' # str | Filters the response by an image status, as a string. For example, ``ACTIVE``.  (optional)
min_disk = 56 # int | Filters the response by a minimum disk space, in GiB. For example, ``100``.  (optional)
min_ram = 56 # int | Filters the response by a minimum RAM, in MiB. For example, ``512``.  (optional)
type = 'type_example' # str | Filters the response by an image type. For example, ``snapshot`` or ``backup``.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)

try:
    api_instance.v21_images_detail_get(changes_since=changes_since, server=server, name=name, status=status, min_disk=min_disk, min_ram=min_ram, type=type, limit=limit, marker=marker)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changes_since** | **str**| Filters the response by a date and time when the image last changed status. Use this query parameter to check for changes since a previous request rather than re-downloading and re-parsing the full status at each polling interval. If data has changed, the call returns only the items changed since the &#x60;&#x60;changes-since&#x60;&#x60; time. If data has not changed since the &#x60;&#x60;changes-since&#x60;&#x60; time, the call returns an empty list. To enable you to keep track of changes, this filter also displays images that were deleted if the &#x60;&#x60;changes-since&#x60;&#x60; value specifies a date in the last 30 days. Items deleted more than 30 days ago might be returned, but it is not guaranteed. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_:  ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  | [optional] 
 **server** | **str**| Filters the response by a server, as a URL.  | [optional] 
 **name** | **str**| Filters the response by an image name, as a string.  | [optional] 
 **status** | **str**| Filters the response by an image status, as a string. For example, &#x60;&#x60;ACTIVE&#x60;&#x60;.  | [optional] 
 **min_disk** | **int**| Filters the response by a minimum disk space, in GiB. For example, &#x60;&#x60;100&#x60;&#x60;.  | [optional] 
 **min_ram** | **int**| Filters the response by a minimum RAM, in MiB. For example, &#x60;&#x60;512&#x60;&#x60;.  | [optional] 
 **type** | **str**| Filters the response by an image type. For example, &#x60;&#x60;snapshot&#x60;&#x60; or &#x60;&#x60;backup&#x60;&#x60;.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_get**
> v21_images_get(changes_since=changes_since, server=server, name=name, status=status, min_disk=min_disk, min_ram=min_ram, type=type, limit=limit, marker=marker)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
changes_since = 'changes_since_example' # str | Filters the response by a date and time when the image last changed status. Use this query parameter to check for changes since a previous request rather than re-downloading and re-parsing the full status at each polling interval. If data has changed, the call returns only the items changed since the ``changes-since`` time. If data has not changed since the ``changes-since`` time, the call returns an empty list. To enable you to keep track of changes, this filter also displays images that were deleted if the ``changes-since`` value specifies a date in the last 30 days. Items deleted more than 30 days ago might be returned, but it is not guaranteed. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_:  ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  (optional)
server = 'server_example' # str | Filters the response by a server, as a URL.  (optional)
name = 'name_example' # str | Filters the response by an image name, as a string.  (optional)
status = 'status_example' # str | Filters the response by an image status, as a string. For example, ``ACTIVE``.  (optional)
min_disk = 56 # int | Filters the response by a minimum disk space, in GiB. For example, ``100``.  (optional)
min_ram = 56 # int | Filters the response by a minimum RAM, in MiB. For example, ``512``.  (optional)
type = 'type_example' # str | Filters the response by an image type. For example, ``snapshot`` or ``backup``.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)

try:
    api_instance.v21_images_get(changes_since=changes_since, server=server, name=name, status=status, min_disk=min_disk, min_ram=min_ram, type=type, limit=limit, marker=marker)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changes_since** | **str**| Filters the response by a date and time when the image last changed status. Use this query parameter to check for changes since a previous request rather than re-downloading and re-parsing the full status at each polling interval. If data has changed, the call returns only the items changed since the &#x60;&#x60;changes-since&#x60;&#x60; time. If data has not changed since the &#x60;&#x60;changes-since&#x60;&#x60; time, the call returns an empty list. To enable you to keep track of changes, this filter also displays images that were deleted if the &#x60;&#x60;changes-since&#x60;&#x60; value specifies a date in the last 30 days. Items deleted more than 30 days ago might be returned, but it is not guaranteed. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_:  ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  | [optional] 
 **server** | **str**| Filters the response by a server, as a URL.  | [optional] 
 **name** | **str**| Filters the response by an image name, as a string.  | [optional] 
 **status** | **str**| Filters the response by an image status, as a string. For example, &#x60;&#x60;ACTIVE&#x60;&#x60;.  | [optional] 
 **min_disk** | **int**| Filters the response by a minimum disk space, in GiB. For example, &#x60;&#x60;100&#x60;&#x60;.  | [optional] 
 **min_ram** | **int**| Filters the response by a minimum RAM, in MiB. For example, &#x60;&#x60;512&#x60;&#x60;.  | [optional] 
 **type** | **str**| Filters the response by an image type. For example, &#x60;&#x60;snapshot&#x60;&#x60; or &#x60;&#x60;backup&#x60;&#x60;.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_delete**
> v21_images_image_id_delete(image_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 

try:
    api_instance.v21_images_image_id_delete(image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_get**
> v21_images_image_id_get(image_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 

try:
    api_instance.v21_images_image_id_get(image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_get**
> v21_images_image_id_metadata_get(image_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 

try:
    api_instance.v21_images_image_id_metadata_get(image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_key_delete**
> v21_images_image_id_metadata_key_delete(image_id, key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 

try:
    api_instance.v21_images_image_id_metadata_key_delete(image_id, key)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_key_get**
> v21_images_image_id_metadata_key_get(image_id, key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 

try:
    api_instance.v21_images_image_id_metadata_key_get(image_id, key)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_key_put**
> v21_images_image_id_metadata_key_put(image_id, key, image_meta_key_put_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 
key = 'key_example' # str | The metadata item key, as a string. Maximum length is 255 characters. 
image_meta_key_put_req = swagger_client.ImageMetaKeyPutReq() # ImageMetaKeyPutReq | 

try:
    api_instance.v21_images_image_id_metadata_key_put(image_id, key, image_meta_key_put_req)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 
 **key** | **str**| The metadata item key, as a string. Maximum length is 255 characters.  | 
 **image_meta_key_put_req** | [**ImageMetaKeyPutReq**](ImageMetaKeyPutReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_post**
> v21_images_image_id_metadata_post(image_id, image_metadata_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 
image_metadata_post_req = swagger_client.ImageMetadataPostReq() # ImageMetadataPostReq | 

try:
    api_instance.v21_images_image_id_metadata_post(image_id, image_metadata_post_req)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 
 **image_metadata_post_req** | [**ImageMetadataPostReq**](ImageMetadataPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_images_image_id_metadata_put**
> v21_images_image_id_metadata_put(image_id, image_metadata_put_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_id = 'image_id_example' # str | The UUID of the image. 
image_metadata_put_req = swagger_client.ImageMetadataPutReq() # ImageMetadataPutReq | 

try:
    api_instance.v21_images_image_id_metadata_put(image_id, image_metadata_put_req)
except ApiException as e:
    print("Exception when calling ImagesApi->v21_images_image_id_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| The UUID of the image.  | 
 **image_metadata_put_req** | [**ImageMetadataPutReq**](ImageMetadataPutReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


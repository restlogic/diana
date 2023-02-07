# swagger_client.OsVolumeAttachmentsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_os_volume_attachments_get**](OsVolumeAttachmentsApi.md#v21_servers_server_id_os_volume_attachments_get) | **GET** /v2.1/servers/{server_id}/os-volume_attachments | 
[**v21_servers_server_id_os_volume_attachments_post**](OsVolumeAttachmentsApi.md#v21_servers_server_id_os_volume_attachments_post) | **POST** /v2.1/servers/{server_id}/os-volume_attachments | 
[**v21_servers_server_id_os_volume_attachments_volume_id_delete**](OsVolumeAttachmentsApi.md#v21_servers_server_id_os_volume_attachments_volume_id_delete) | **DELETE** /v2.1/servers/{server_id}/os-volume_attachments/{volume_id} | 
[**v21_servers_server_id_os_volume_attachments_volume_id_get**](OsVolumeAttachmentsApi.md#v21_servers_server_id_os_volume_attachments_volume_id_get) | **GET** /v2.1/servers/{server_id}/os-volume_attachments/{volume_id} | 
[**v21_servers_server_id_os_volume_attachments_volume_id_put**](OsVolumeAttachmentsApi.md#v21_servers_server_id_os_volume_attachments_volume_id_put) | **PUT** /v2.1/servers/{server_id}/os-volume_attachments/{volume_id} | 


# **v21_servers_server_id_os_volume_attachments_get**
> v21_servers_server_id_os_volume_attachments_get(server_id, limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumeAttachmentsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_servers_server_id_os_volume_attachments_get(server_id, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsVolumeAttachmentsApi->v21_servers_server_id_os_volume_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
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

# **v21_servers_server_id_os_volume_attachments_post**
> v21_servers_server_id_os_volume_attachments_post(server_id, attach_volume_to_server_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumeAttachmentsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
attach_volume_to_server_req = swagger_client.AttachVolumeToServerReq() # AttachVolumeToServerReq | 

try:
    api_instance.v21_servers_server_id_os_volume_attachments_post(server_id, attach_volume_to_server_req)
except ApiException as e:
    print("Exception when calling OsVolumeAttachmentsApi->v21_servers_server_id_os_volume_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **attach_volume_to_server_req** | [**AttachVolumeToServerReq**](AttachVolumeToServerReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_volume_attachments_volume_id_delete**
> v21_servers_server_id_os_volume_attachments_volume_id_delete(server_id, volume_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumeAttachmentsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
volume_id = 'volume_id_example' # str | The UUID of the volume to detach. 

try:
    api_instance.v21_servers_server_id_os_volume_attachments_volume_id_delete(server_id, volume_id)
except ApiException as e:
    print("Exception when calling OsVolumeAttachmentsApi->v21_servers_server_id_os_volume_attachments_volume_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **volume_id** | **str**| The UUID of the volume to detach.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_volume_attachments_volume_id_get**
> v21_servers_server_id_os_volume_attachments_volume_id_get(server_id, volume_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumeAttachmentsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
volume_id = 'volume_id_example' # str | The UUID of the attached volume. 

try:
    api_instance.v21_servers_server_id_os_volume_attachments_volume_id_get(server_id, volume_id)
except ApiException as e:
    print("Exception when calling OsVolumeAttachmentsApi->v21_servers_server_id_os_volume_attachments_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **volume_id** | **str**| The UUID of the attached volume.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_os_volume_attachments_volume_id_put**
> v21_servers_server_id_os_volume_attachments_volume_id_put(server_id, volume_id, update_volume_attachment_delete_flag_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsVolumeAttachmentsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
volume_id = 'volume_id_example' # str | The UUID of the volume being replaced. 
update_volume_attachment_delete_flag_req = swagger_client.UpdateVolumeAttachmentDeleteFlagReq() # UpdateVolumeAttachmentDeleteFlagReq | 

try:
    api_instance.v21_servers_server_id_os_volume_attachments_volume_id_put(server_id, volume_id, update_volume_attachment_delete_flag_req)
except ApiException as e:
    print("Exception when calling OsVolumeAttachmentsApi->v21_servers_server_id_os_volume_attachments_volume_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **volume_id** | **str**| The UUID of the volume being replaced.  | 
 **update_volume_attachment_delete_flag_req** | [**UpdateVolumeAttachmentDeleteFlagReq**](UpdateVolumeAttachmentDeleteFlagReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.OsAssistedVolumeSnapshotsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_assisted_volume_snapshots_post**](OsAssistedVolumeSnapshotsApi.md#v21_os_assisted_volume_snapshots_post) | **POST** /v2.1/os-assisted-volume-snapshots | 
[**v21_os_assisted_volume_snapshots_snapshot_id_delete**](OsAssistedVolumeSnapshotsApi.md#v21_os_assisted_volume_snapshots_snapshot_id_delete) | **DELETE** /v2.1/os-assisted-volume-snapshots/{snapshot_id} | 


# **v21_os_assisted_volume_snapshots_post**
> v21_os_assisted_volume_snapshots_post(snapshot_create_assisted_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAssistedVolumeSnapshotsApi()
snapshot_create_assisted_req = swagger_client.SnapshotCreateAssistedReq() # SnapshotCreateAssistedReq | 

try:
    api_instance.v21_os_assisted_volume_snapshots_post(snapshot_create_assisted_req)
except ApiException as e:
    print("Exception when calling OsAssistedVolumeSnapshotsApi->v21_os_assisted_volume_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_create_assisted_req** | [**SnapshotCreateAssistedReq**](SnapshotCreateAssistedReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_assisted_volume_snapshots_snapshot_id_delete**
> v21_os_assisted_volume_snapshots_snapshot_id_delete(snapshot_id, delete_info)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAssistedVolumeSnapshotsApi()
snapshot_id = 'snapshot_id_example' # str | The UUID of the snapshot. 
delete_info = 'delete_info_example' # str | Information for snapshot deletion. Include the ID of the associated volume. For example:  .. code-block:: javascript     DELETE /os-assisted-volume-snapshots/421752a6-acf6-4b2d-bc7a-119f9148cd8c?delete_info='{\"volume_id\": \"521752a6-acf6-4b2d-bc7a-119f9148cd8c\"}' 

try:
    api_instance.v21_os_assisted_volume_snapshots_snapshot_id_delete(snapshot_id, delete_info)
except ApiException as e:
    print("Exception when calling OsAssistedVolumeSnapshotsApi->v21_os_assisted_volume_snapshots_snapshot_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The UUID of the snapshot.  | 
 **delete_info** | **str**| Information for snapshot deletion. Include the ID of the associated volume. For example:  .. code-block:: javascript     DELETE /os-assisted-volume-snapshots/421752a6-acf6-4b2d-bc7a-119f9148cd8c?delete_info&#x3D;&#39;{\&quot;volume_id\&quot;: \&quot;521752a6-acf6-4b2d-bc7a-119f9148cd8c\&quot;}&#39;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


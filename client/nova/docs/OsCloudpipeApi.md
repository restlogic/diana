# swagger_client.OsCloudpipeApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_cloudpipe_configure_project_put**](OsCloudpipeApi.md#v21_os_cloudpipe_configure_project_put) | **PUT** /v2.1/os-cloudpipe/configure-project | 
[**v21_os_cloudpipe_get**](OsCloudpipeApi.md#v21_os_cloudpipe_get) | **GET** /v2.1/os-cloudpipe | 
[**v21_os_cloudpipe_post**](OsCloudpipeApi.md#v21_os_cloudpipe_post) | **POST** /v2.1/os-cloudpipe | 


# **v21_os_cloudpipe_configure_project_put**
> v21_os_cloudpipe_configure_project_put(cloud_pipe_update_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCloudpipeApi()
cloud_pipe_update_req = swagger_client.CloudPipeUpdateReq() # CloudPipeUpdateReq | 

try:
    api_instance.v21_os_cloudpipe_configure_project_put(cloud_pipe_update_req)
except ApiException as e:
    print("Exception when calling OsCloudpipeApi->v21_os_cloudpipe_configure_project_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pipe_update_req** | [**CloudPipeUpdateReq**](CloudPipeUpdateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_cloudpipe_get**
> v21_os_cloudpipe_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCloudpipeApi()

try:
    api_instance.v21_os_cloudpipe_get()
except ApiException as e:
    print("Exception when calling OsCloudpipeApi->v21_os_cloudpipe_get: %s\n" % e)
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

# **v21_os_cloudpipe_post**
> v21_os_cloudpipe_post(cloud_pipe_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsCloudpipeApi()
cloud_pipe_create_req = swagger_client.CloudPipeCreateReq() # CloudPipeCreateReq | 

try:
    api_instance.v21_os_cloudpipe_post(cloud_pipe_create_req)
except ApiException as e:
    print("Exception when calling OsCloudpipeApi->v21_os_cloudpipe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pipe_create_req** | [**CloudPipeCreateReq**](CloudPipeCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


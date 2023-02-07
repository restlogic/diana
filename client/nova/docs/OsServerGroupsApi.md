# swagger_client.OsServerGroupsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_server_groups_get**](OsServerGroupsApi.md#v21_os_server_groups_get) | **GET** /v2.1/os-server-groups | 
[**v21_os_server_groups_post**](OsServerGroupsApi.md#v21_os_server_groups_post) | **POST** /v2.1/os-server-groups | 
[**v21_os_server_groups_server_group_id_delete**](OsServerGroupsApi.md#v21_os_server_groups_server_group_id_delete) | **DELETE** /v2.1/os-server-groups/{server_group_id} | 
[**v21_os_server_groups_server_group_id_get**](OsServerGroupsApi.md#v21_os_server_groups_server_group_id_get) | **GET** /v2.1/os-server-groups/{server_group_id} | 


# **v21_os_server_groups_get**
> v21_os_server_groups_get(all_projects=all_projects, limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerGroupsApi()
all_projects = 'all_projects_example' # str | Administrator only. Lists server groups for all projects. For example:    ``GET /os-server-groups?all_projects=True``  If you specify a tenant ID for a non-administrative user with this query parameter, the call lists all server groups for the tenant, or project, rather than for all projects. Value of this query parameter is not checked, only presence is considered as request for all projects.  (optional)
limit = 56 # int | Used in conjunction with ``offset`` to return a slice of items. ``limit`` is the maximum number of items to return. If ``limit`` is not specified, or exceeds the configurable ``max_limit``, then ``max_limit`` will be used instead.  (optional)
offset = 56 # int | Used in conjunction with ``limit`` to return a slice of items. ``offset`` is where to start in the list.  (optional)

try:
    api_instance.v21_os_server_groups_get(all_projects=all_projects, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling OsServerGroupsApi->v21_os_server_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_projects** | **str**| Administrator only. Lists server groups for all projects. For example:    &#x60;&#x60;GET /os-server-groups?all_projects&#x3D;True&#x60;&#x60;  If you specify a tenant ID for a non-administrative user with this query parameter, the call lists all server groups for the tenant, or project, rather than for all projects. Value of this query parameter is not checked, only presence is considered as request for all projects.  | [optional] 
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

# **v21_os_server_groups_post**
> v21_os_server_groups_post(server_groups_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerGroupsApi()
server_groups_post_req = swagger_client.ServerGroupsPostReq() # ServerGroupsPostReq | 

try:
    api_instance.v21_os_server_groups_post(server_groups_post_req)
except ApiException as e:
    print("Exception when calling OsServerGroupsApi->v21_os_server_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_groups_post_req** | [**ServerGroupsPostReq**](ServerGroupsPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_server_groups_server_group_id_delete**
> v21_os_server_groups_server_group_id_delete(server_group_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerGroupsApi()
server_group_id = 'server_group_id_example' # str | The UUID of the server group. 

try:
    api_instance.v21_os_server_groups_server_group_id_delete(server_group_id)
except ApiException as e:
    print("Exception when calling OsServerGroupsApi->v21_os_server_groups_server_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_group_id** | **str**| The UUID of the server group.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_server_groups_server_group_id_get**
> v21_os_server_groups_server_group_id_get(server_group_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsServerGroupsApi()
server_group_id = 'server_group_id_example' # str | The UUID of the server group. 

try:
    api_instance.v21_os_server_groups_server_group_id_get(server_group_id)
except ApiException as e:
    print("Exception when calling OsServerGroupsApi->v21_os_server_groups_server_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_group_id** | **str**| The UUID of the server group.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


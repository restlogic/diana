# swagger_client.OsAgentsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_agents_agent_build_id_delete**](OsAgentsApi.md#v21_os_agents_agent_build_id_delete) | **DELETE** /v2.1/os-agents/{agent_build_id} | 
[**v21_os_agents_agent_build_id_put**](OsAgentsApi.md#v21_os_agents_agent_build_id_put) | **PUT** /v2.1/os-agents/{agent_build_id} | 
[**v21_os_agents_get**](OsAgentsApi.md#v21_os_agents_get) | **GET** /v2.1/os-agents | 
[**v21_os_agents_post**](OsAgentsApi.md#v21_os_agents_post) | **POST** /v2.1/os-agents | 


# **v21_os_agents_agent_build_id_delete**
> v21_os_agents_agent_build_id_delete(agent_build_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAgentsApi()
agent_build_id = 'agent_build_id_example' # str | The id of the agent build. 

try:
    api_instance.v21_os_agents_agent_build_id_delete(agent_build_id)
except ApiException as e:
    print("Exception when calling OsAgentsApi->v21_os_agents_agent_build_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_build_id** | **str**| The id of the agent build.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_agents_agent_build_id_put**
> v21_os_agents_agent_build_id_put(agent_build_id, agent_update_put_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAgentsApi()
agent_build_id = 'agent_build_id_example' # str | The id of the agent build. 
agent_update_put_req = swagger_client.AgentUpdatePutReq() # AgentUpdatePutReq | 

try:
    api_instance.v21_os_agents_agent_build_id_put(agent_build_id, agent_update_put_req)
except ApiException as e:
    print("Exception when calling OsAgentsApi->v21_os_agents_agent_build_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_build_id** | **str**| The id of the agent build.  | 
 **agent_update_put_req** | [**AgentUpdatePutReq**](AgentUpdatePutReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_agents_get**
> v21_os_agents_get(hypervisor=hypervisor)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAgentsApi()
hypervisor = 'hypervisor_example' # str | Filters the response by a hypervisor type.  (optional)

try:
    api_instance.v21_os_agents_get(hypervisor=hypervisor)
except ApiException as e:
    print("Exception when calling OsAgentsApi->v21_os_agents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hypervisor** | **str**| Filters the response by a hypervisor type.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_agents_post**
> v21_os_agents_post(agent_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsAgentsApi()
agent_post_req = swagger_client.AgentPostReq() # AgentPostReq | 

try:
    api_instance.v21_os_agents_post(agent_post_req)
except ApiException as e:
    print("Exception when calling OsAgentsApi->v21_os_agents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_post_req** | [**AgentPostReq**](AgentPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


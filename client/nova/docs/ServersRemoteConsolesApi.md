# swagger_client.ServersRemoteConsolesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_console_auth_tokens_console_token_get**](ServersRemoteConsolesApi.md#v21_os_console_auth_tokens_console_token_get) | **GET** /v2.1/os-console-auth-tokens/{console_token} | 
[**v21_servers_server_id_remote_consoles_post**](ServersRemoteConsolesApi.md#v21_servers_server_id_remote_consoles_post) | **POST** /v2.1/servers/{server_id}/remote-consoles | 


# **v21_os_console_auth_tokens_console_token_get**
> v21_os_console_auth_tokens_console_token_get(console_token)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersRemoteConsolesApi()
console_token = 'console_token_example' # str | Console authentication token. 

try:
    api_instance.v21_os_console_auth_tokens_console_token_get(console_token)
except ApiException as e:
    print("Exception when calling ServersRemoteConsolesApi->v21_os_console_auth_tokens_console_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **console_token** | **str**| Console authentication token.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_remote_consoles_post**
> v21_servers_server_id_remote_consoles_post(server_id, create_vnc_console_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersRemoteConsolesApi()
server_id = 'server_id_example' # str | The UUID of the server. 
create_vnc_console_req = swagger_client.CreateVncConsoleReq() # CreateVncConsoleReq | 

try:
    api_instance.v21_servers_server_id_remote_consoles_post(server_id, create_vnc_console_req)
except ApiException as e:
    print("Exception when calling ServersRemoteConsolesApi->v21_servers_server_id_remote_consoles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **create_vnc_console_req** | [**CreateVncConsoleReq**](CreateVncConsoleReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


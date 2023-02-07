# swagger_client.ServerMigrationsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_server_id_migrations_get**](ServerMigrationsApi.md#v21_servers_server_id_migrations_get) | **GET** /v2.1/servers/{server_id}/migrations | 
[**v21_servers_server_id_migrations_migration_id_action_post**](ServerMigrationsApi.md#v21_servers_server_id_migrations_migration_id_action_post) | **POST** /v2.1/servers/{server_id}/migrations/{migration_id}/action | 
[**v21_servers_server_id_migrations_migration_id_delete**](ServerMigrationsApi.md#v21_servers_server_id_migrations_migration_id_delete) | **DELETE** /v2.1/servers/{server_id}/migrations/{migration_id} | 
[**v21_servers_server_id_migrations_migration_id_get**](ServerMigrationsApi.md#v21_servers_server_id_migrations_migration_id_get) | **GET** /v2.1/servers/{server_id}/migrations/{migration_id} | 


# **v21_servers_server_id_migrations_get**
> v21_servers_server_id_migrations_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerMigrationsApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_migrations_get(server_id)
except ApiException as e:
    print("Exception when calling ServerMigrationsApi->v21_servers_server_id_migrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_migrations_migration_id_action_post**
> v21_servers_server_id_migrations_migration_id_action_post(server_id, migration_id, force_complete)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerMigrationsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
migration_id = 56 # int | The ID of the server migration. 
force_complete = swagger_client.ForceComplete() # ForceComplete | 

try:
    api_instance.v21_servers_server_id_migrations_migration_id_action_post(server_id, migration_id, force_complete)
except ApiException as e:
    print("Exception when calling ServerMigrationsApi->v21_servers_server_id_migrations_migration_id_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **migration_id** | **int**| The ID of the server migration.  | 
 **force_complete** | [**ForceComplete**](ForceComplete.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_migrations_migration_id_delete**
> v21_servers_server_id_migrations_migration_id_delete(server_id, migration_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerMigrationsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
migration_id = 56 # int | The ID of the server migration. 

try:
    api_instance.v21_servers_server_id_migrations_migration_id_delete(server_id, migration_id)
except ApiException as e:
    print("Exception when calling ServerMigrationsApi->v21_servers_server_id_migrations_migration_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **migration_id** | **int**| The ID of the server migration.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_migrations_migration_id_get**
> v21_servers_server_id_migrations_migration_id_get(server_id, migration_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerMigrationsApi()
server_id = 'server_id_example' # str | The UUID of the server. 
migration_id = 56 # int | The ID of the server migration. 

try:
    api_instance.v21_servers_server_id_migrations_migration_id_get(server_id, migration_id)
except ApiException as e:
    print("Exception when calling ServerMigrationsApi->v21_servers_server_id_migrations_migration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **migration_id** | **int**| The ID of the server migration.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.OsFlavorAccessApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_flavors_flavor_id_action_post**](OsFlavorAccessApi.md#v21_flavors_flavor_id_action_post) | **POST** /v2.1/flavors/{flavor_id}/action | 
[**v21_flavors_flavor_id_os_flavor_access_get**](OsFlavorAccessApi.md#v21_flavors_flavor_id_os_flavor_access_get) | **GET** /v2.1/flavors/{flavor_id}/os-flavor-access | 


# **v21_flavors_flavor_id_action_post**
> v21_flavors_flavor_id_action_post(flavor_id, flavor_access_add_tenant_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorAccessApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_access_add_tenant_req = swagger_client.FlavorAccessAddTenantReq() # FlavorAccessAddTenantReq | 

try:
    api_instance.v21_flavors_flavor_id_action_post(flavor_id, flavor_access_add_tenant_req)
except ApiException as e:
    print("Exception when calling OsFlavorAccessApi->v21_flavors_flavor_id_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_access_add_tenant_req** | [**FlavorAccessAddTenantReq**](FlavorAccessAddTenantReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_os_flavor_access_get**
> v21_flavors_flavor_id_os_flavor_access_get(flavor_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorAccessApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 

try:
    api_instance.v21_flavors_flavor_id_os_flavor_access_get(flavor_id)
except ApiException as e:
    print("Exception when calling OsFlavorAccessApi->v21_flavors_flavor_id_os_flavor_access_get: %s\n" % e)
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


# swagger_client.OsFlavorExtraSpecsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete**](OsFlavorExtraSpecsApi.md#v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete) | **DELETE** /v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key} | 
[**v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get**](OsFlavorExtraSpecsApi.md#v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get) | **GET** /v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key} | 
[**v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put**](OsFlavorExtraSpecsApi.md#v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put) | **PUT** /v2.1/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key} | 
[**v21_flavors_flavor_id_os_extra_specs_get**](OsFlavorExtraSpecsApi.md#v21_flavors_flavor_id_os_extra_specs_get) | **GET** /v2.1/flavors/{flavor_id}/os-extra_specs | 
[**v21_flavors_flavor_id_os_extra_specs_post**](OsFlavorExtraSpecsApi.md#v21_flavors_flavor_id_os_extra_specs_post) | **POST** /v2.1/flavors/{flavor_id}/os-extra_specs | 


# **v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete**
> v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete(flavor_id, flavor_extra_spec_key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorExtraSpecsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_extra_spec_key = 'flavor_extra_spec_key_example' # str | The extra spec key for the flavor. 

try:
    api_instance.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete(flavor_id, flavor_extra_spec_key)
except ApiException as e:
    print("Exception when calling OsFlavorExtraSpecsApi->v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_extra_spec_key** | **str**| The extra spec key for the flavor.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get**
> v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get(flavor_id, flavor_extra_spec_key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorExtraSpecsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_extra_spec_key = 'flavor_extra_spec_key_example' # str | The extra spec key for the flavor. 

try:
    api_instance.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get(flavor_id, flavor_extra_spec_key)
except ApiException as e:
    print("Exception when calling OsFlavorExtraSpecsApi->v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_extra_spec_key** | **str**| The extra spec key for the flavor.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put**
> v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorExtraSpecsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_extra_spec_key = 'flavor_extra_spec_key_example' # str | The extra spec key for the flavor. 
flavor_extra_specs_update_req = swagger_client.FlavorExtraSpecsUpdateReq() # FlavorExtraSpecsUpdateReq | 

try:
    api_instance.v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put(flavor_id, flavor_extra_spec_key, flavor_extra_specs_update_req)
except ApiException as e:
    print("Exception when calling OsFlavorExtraSpecsApi->v21_flavors_flavor_id_os_extra_specs_flavor_extra_spec_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_extra_spec_key** | **str**| The extra spec key for the flavor.  | 
 **flavor_extra_specs_update_req** | [**FlavorExtraSpecsUpdateReq**](FlavorExtraSpecsUpdateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_flavors_flavor_id_os_extra_specs_get**
> v21_flavors_flavor_id_os_extra_specs_get(flavor_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorExtraSpecsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 

try:
    api_instance.v21_flavors_flavor_id_os_extra_specs_get(flavor_id)
except ApiException as e:
    print("Exception when calling OsFlavorExtraSpecsApi->v21_flavors_flavor_id_os_extra_specs_get: %s\n" % e)
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

# **v21_flavors_flavor_id_os_extra_specs_post**
> v21_flavors_flavor_id_os_extra_specs_post(flavor_id, flavor_extra_specs_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsFlavorExtraSpecsApi()
flavor_id = 'flavor_id_example' # str | The ID of the flavor. 
flavor_extra_specs_create_req = swagger_client.FlavorExtraSpecsCreateReq() # FlavorExtraSpecsCreateReq | 

try:
    api_instance.v21_flavors_flavor_id_os_extra_specs_post(flavor_id, flavor_extra_specs_create_req)
except ApiException as e:
    print("Exception when calling OsFlavorExtraSpecsApi->v21_flavors_flavor_id_os_extra_specs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor_id** | **str**| The ID of the flavor.  | 
 **flavor_extra_specs_create_req** | [**FlavorExtraSpecsCreateReq**](FlavorExtraSpecsCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


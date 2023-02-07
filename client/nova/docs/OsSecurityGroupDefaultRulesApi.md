# swagger_client.OsSecurityGroupDefaultRulesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_security_group_default_rules_get**](OsSecurityGroupDefaultRulesApi.md#v21_os_security_group_default_rules_get) | **GET** /v2.1/os-security-group-default-rules | 
[**v21_os_security_group_default_rules_post**](OsSecurityGroupDefaultRulesApi.md#v21_os_security_group_default_rules_post) | **POST** /v2.1/os-security-group-default-rules | 
[**v21_os_security_group_default_rules_security_group_default_rule_id_delete**](OsSecurityGroupDefaultRulesApi.md#v21_os_security_group_default_rules_security_group_default_rule_id_delete) | **DELETE** /v2.1/os-security-group-default-rules/{security_group_default_rule_id} | 
[**v21_os_security_group_default_rules_security_group_default_rule_id_get**](OsSecurityGroupDefaultRulesApi.md#v21_os_security_group_default_rules_security_group_default_rule_id_get) | **GET** /v2.1/os-security-group-default-rules/{security_group_default_rule_id} | 


# **v21_os_security_group_default_rules_get**
> v21_os_security_group_default_rules_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupDefaultRulesApi()

try:
    api_instance.v21_os_security_group_default_rules_get()
except ApiException as e:
    print("Exception when calling OsSecurityGroupDefaultRulesApi->v21_os_security_group_default_rules_get: %s\n" % e)
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

# **v21_os_security_group_default_rules_post**
> v21_os_security_group_default_rules_post(security_group_default_rules_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupDefaultRulesApi()
security_group_default_rules_create_req = swagger_client.SecurityGroupDefaultRulesCreateReq() # SecurityGroupDefaultRulesCreateReq | 

try:
    api_instance.v21_os_security_group_default_rules_post(security_group_default_rules_create_req)
except ApiException as e:
    print("Exception when calling OsSecurityGroupDefaultRulesApi->v21_os_security_group_default_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_default_rules_create_req** | [**SecurityGroupDefaultRulesCreateReq**](SecurityGroupDefaultRulesCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_security_group_default_rules_security_group_default_rule_id_delete**
> v21_os_security_group_default_rules_security_group_default_rule_id_delete(security_group_default_rule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupDefaultRulesApi()
security_group_default_rule_id = 'security_group_default_rule_id_example' # str | The UUID of the security group rule. 

try:
    api_instance.v21_os_security_group_default_rules_security_group_default_rule_id_delete(security_group_default_rule_id)
except ApiException as e:
    print("Exception when calling OsSecurityGroupDefaultRulesApi->v21_os_security_group_default_rules_security_group_default_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_default_rule_id** | **str**| The UUID of the security group rule.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_security_group_default_rules_security_group_default_rule_id_get**
> v21_os_security_group_default_rules_security_group_default_rule_id_get(security_group_default_rule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupDefaultRulesApi()
security_group_default_rule_id = 'security_group_default_rule_id_example' # str | The UUID of the security group rule. 

try:
    api_instance.v21_os_security_group_default_rules_security_group_default_rule_id_get(security_group_default_rule_id)
except ApiException as e:
    print("Exception when calling OsSecurityGroupDefaultRulesApi->v21_os_security_group_default_rules_security_group_default_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_default_rule_id** | **str**| The UUID of the security group rule.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


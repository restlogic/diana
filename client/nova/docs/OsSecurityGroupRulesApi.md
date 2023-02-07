# swagger_client.OsSecurityGroupRulesApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_security_group_rules_post**](OsSecurityGroupRulesApi.md#v21_os_security_group_rules_post) | **POST** /v2.1/os-security-group-rules | 
[**v21_os_security_group_rules_security_group_rule_id_delete**](OsSecurityGroupRulesApi.md#v21_os_security_group_rules_security_group_rule_id_delete) | **DELETE** /v2.1/os-security-group-rules/{security_group_rule_id} | 


# **v21_os_security_group_rules_post**
> v21_os_security_group_rules_post(security_group_rules_post_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupRulesApi()
security_group_rules_post_req = swagger_client.SecurityGroupRulesPostReq() # SecurityGroupRulesPostReq | 

try:
    api_instance.v21_os_security_group_rules_post(security_group_rules_post_req)
except ApiException as e:
    print("Exception when calling OsSecurityGroupRulesApi->v21_os_security_group_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_rules_post_req** | [**SecurityGroupRulesPostReq**](SecurityGroupRulesPostReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_security_group_rules_security_group_rule_id_delete**
> v21_os_security_group_rules_security_group_rule_id_delete(security_group_rule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSecurityGroupRulesApi()
security_group_rule_id = 'security_group_rule_id_example' # str | The ID of the security group rule. 

try:
    api_instance.v21_os_security_group_rules_security_group_rule_id_delete(security_group_rule_id)
except ApiException as e:
    print("Exception when calling OsSecurityGroupRulesApi->v21_os_security_group_rules_security_group_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_group_rule_id** | **str**| The ID of the security group rule.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


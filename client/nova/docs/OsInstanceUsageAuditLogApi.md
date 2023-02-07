# swagger_client.OsInstanceUsageAuditLogApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_instance_usage_audit_log_before_timestamp_get**](OsInstanceUsageAuditLogApi.md#v21_os_instance_usage_audit_log_before_timestamp_get) | **GET** /v2.1/os-instance_usage_audit_log/{before_timestamp} | 
[**v21_os_instance_usage_audit_log_get**](OsInstanceUsageAuditLogApi.md#v21_os_instance_usage_audit_log_get) | **GET** /v2.1/os-instance_usage_audit_log | 


# **v21_os_instance_usage_audit_log_before_timestamp_get**
> v21_os_instance_usage_audit_log_before_timestamp_get(before_timestamp)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInstanceUsageAuditLogApi()
before_timestamp = 'before_timestamp_example' # str | Filters the response by the date and time before which to list usage audits. The date and time stamp format is as follows:  ::    CCYY-MM-DD hh:mm:ss.NNNNNN  For example, ``2015-08-27 09:49:58`` or ``2015-08-27 09:49:58.123456``. 

try:
    api_instance.v21_os_instance_usage_audit_log_before_timestamp_get(before_timestamp)
except ApiException as e:
    print("Exception when calling OsInstanceUsageAuditLogApi->v21_os_instance_usage_audit_log_before_timestamp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before_timestamp** | **str**| Filters the response by the date and time before which to list usage audits. The date and time stamp format is as follows:  ::    CCYY-MM-DD hh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27 09:49:58&#x60;&#x60; or &#x60;&#x60;2015-08-27 09:49:58.123456&#x60;&#x60;.  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_instance_usage_audit_log_get**
> v21_os_instance_usage_audit_log_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsInstanceUsageAuditLogApi()

try:
    api_instance.v21_os_instance_usage_audit_log_get()
except ApiException as e:
    print("Exception when calling OsInstanceUsageAuditLogApi->v21_os_instance_usage_audit_log_get: %s\n" % e)
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


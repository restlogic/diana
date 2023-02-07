# swagger_client.OsSimpleTenantUsageApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_simple_tenant_usage_get**](OsSimpleTenantUsageApi.md#v21_os_simple_tenant_usage_get) | **GET** /v2.1/os-simple-tenant-usage | 
[**v21_os_simple_tenant_usage_tenant_id_get**](OsSimpleTenantUsageApi.md#v21_os_simple_tenant_usage_tenant_id_get) | **GET** /v2.1/os-simple-tenant-usage/{tenant_id} | 


# **v21_os_simple_tenant_usage_get**
> v21_os_simple_tenant_usage_get(detailed=detailed, end=end, start=start, limit=limit, marker=marker)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSimpleTenantUsageApi()
detailed = 56 # int | Specify the ``detailed=1`` query parameter to get detail information ('server_usages' information).  (optional)
end = 'end_example' # str | The ending time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, ``2015-08-27T09:49:58``.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, ``2015-08-27T09:49:58.123456``.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, ``2015-08-27 09:49:58.123456``. If you omit this parameter, the current time is used.  (optional)
start = 'start_example' # str | The beginning time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, ``2015-08-27T09:49:58``.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, ``2015-08-27T09:49:58.123456``.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, ``2015-08-27 09:49:58.123456``. If you omit this parameter, the current time is used.  (optional)
limit = 56 # int | Requests a page size of items. Calculate usage for the limited number of instances. Use the ``limit`` parameter to make an initial limited request and use the last-seen instance UUID from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The last-seen item. Use the ``limit`` parameter to make an initial limited request and use the last-seen instance UUID from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)

try:
    api_instance.v21_os_simple_tenant_usage_get(detailed=detailed, end=end, start=start, limit=limit, marker=marker)
except ApiException as e:
    print("Exception when calling OsSimpleTenantUsageApi->v21_os_simple_tenant_usage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detailed** | **int**| Specify the &#x60;&#x60;detailed&#x3D;1&#x60;&#x60; query parameter to get detail information (&#39;server_usages&#39; information).  | [optional] 
 **end** | **str**| The ending time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, &#x60;&#x60;2015-08-27T09:49:58&#x60;&#x60;.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27T09:49:58.123456&#x60;&#x60;.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27 09:49:58.123456&#x60;&#x60;. If you omit this parameter, the current time is used.  | [optional] 
 **start** | **str**| The beginning time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, &#x60;&#x60;2015-08-27T09:49:58&#x60;&#x60;.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27T09:49:58.123456&#x60;&#x60;.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27 09:49:58.123456&#x60;&#x60;. If you omit this parameter, the current time is used.  | [optional] 
 **limit** | **int**| Requests a page size of items. Calculate usage for the limited number of instances. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen instance UUID from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen instance UUID from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_os_simple_tenant_usage_tenant_id_get**
> v21_os_simple_tenant_usage_tenant_id_get(tenant_id, end=end, start=start, limit=limit, marker=marker)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsSimpleTenantUsageApi()
tenant_id = 'tenant_id_example' # str | The UUID of the tenant in a multi-tenancy cloud. 
end = 'end_example' # str | The ending time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, ``2015-08-27T09:49:58``.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, ``2015-08-27T09:49:58.123456``.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, ``2015-08-27 09:49:58.123456``. If you omit this parameter, the current time is used.  (optional)
start = 'start_example' # str | The beginning time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, ``2015-08-27T09:49:58``.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, ``2015-08-27T09:49:58.123456``.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, ``2015-08-27 09:49:58.123456``. If you omit this parameter, the current time is used.  (optional)
limit = 56 # int | Requests a page size of items. Calculate usage for the limited number of instances. Use the ``limit`` parameter to make an initial limited request and use the last-seen instance UUID from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The last-seen item. Use the ``limit`` parameter to make an initial limited request and use the last-seen instance UUID from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)

try:
    api_instance.v21_os_simple_tenant_usage_tenant_id_get(tenant_id, end=end, start=start, limit=limit, marker=marker)
except ApiException as e:
    print("Exception when calling OsSimpleTenantUsageApi->v21_os_simple_tenant_usage_tenant_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The UUID of the tenant in a multi-tenancy cloud.  | 
 **end** | **str**| The ending time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, &#x60;&#x60;2015-08-27T09:49:58&#x60;&#x60;.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27T09:49:58.123456&#x60;&#x60;.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27 09:49:58.123456&#x60;&#x60;. If you omit this parameter, the current time is used.  | [optional] 
 **start** | **str**| The beginning time to calculate usage statistics on compute and storage resources. The date and time stamp format is any of the following ones:  ::     CCYY-MM-DDThh:mm:ss  For example, &#x60;&#x60;2015-08-27T09:49:58&#x60;&#x60;.  ::     CCYY-MM-DDThh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27T09:49:58.123456&#x60;&#x60;.  ::     CCYY-MM-DD hh:mm:ss.NNNNNN  For example, &#x60;&#x60;2015-08-27 09:49:58.123456&#x60;&#x60;. If you omit this parameter, the current time is used.  | [optional] 
 **limit** | **int**| Requests a page size of items. Calculate usage for the limited number of instances. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen instance UUID from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen instance UUID from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


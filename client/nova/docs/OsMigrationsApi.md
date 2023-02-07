# swagger_client.OsMigrationsApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_os_migrations_get**](OsMigrationsApi.md#v21_os_migrations_get) | **GET** /v2.1/os-migrations | 


# **v21_os_migrations_get**
> v21_os_migrations_get(hidden=hidden, host=host, instance_uuid=instance_uuid, migration_type=migration_type, source_compute=source_compute, status=status, limit=limit, marker=marker, changes_since=changes_since, changes_before=changes_before, user_id=user_id, project_id=project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OsMigrationsApi()
hidden = 56 # int | The 'hidden' setting of migration to filter. The 'hidden' flag is set if the value is 1. The 'hidden' flag is not set if the value is 0. But the 'hidden' setting of migration is always 0, so this parameter is useless to filter migrations.  (optional)
host = 'host_example' # str | The source/destination compute node of migration to filter.  (optional)
instance_uuid = 'instance_uuid_example' # str | The uuid of the instance that migration is operated on to filter.  (optional)
migration_type = 'migration_type_example' # str | The type of migration to filter. Valid values are:  * ``evacuation`` * ``live-migration`` * ``migration`` * ``resize``  (optional)
source_compute = 'source_compute_example' # str | The source compute node of migration to filter.  (optional)
status = 'status_example' # str | The status of migration to filter.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
marker = 'marker_example' # str | The UUID of the last-seen migration. Use the ``limit`` parameter to make an initial limited request and use the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
changes_since = 'changes_since_example' # str | Filters the response by a date and time stamp when the migration last changed. Those changed after the specified date and time stamp are returned.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400.  (optional)
changes_before = 'changes_before_example' # str | Filters the response by a date and time stamp when the migration last changed. Those migrations that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400.  (optional)
user_id = 'user_id_example' # str | Filter the migrations by the given user ID.  (optional)
project_id = 'project_id_example' # str | Filter the migrations by the given project ID.  (optional)

try:
    api_instance.v21_os_migrations_get(hidden=hidden, host=host, instance_uuid=instance_uuid, migration_type=migration_type, source_compute=source_compute, status=status, limit=limit, marker=marker, changes_since=changes_since, changes_before=changes_before, user_id=user_id, project_id=project_id)
except ApiException as e:
    print("Exception when calling OsMigrationsApi->v21_os_migrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hidden** | **int**| The &#39;hidden&#39; setting of migration to filter. The &#39;hidden&#39; flag is set if the value is 1. The &#39;hidden&#39; flag is not set if the value is 0. But the &#39;hidden&#39; setting of migration is always 0, so this parameter is useless to filter migrations.  | [optional] 
 **host** | **str**| The source/destination compute node of migration to filter.  | [optional] 
 **instance_uuid** | **str**| The uuid of the instance that migration is operated on to filter.  | [optional] 
 **migration_type** | **str**| The type of migration to filter. Valid values are:  * &#x60;&#x60;evacuation&#x60;&#x60; * &#x60;&#x60;live-migration&#x60;&#x60; * &#x60;&#x60;migration&#x60;&#x60; * &#x60;&#x60;resize&#x60;&#x60;  | [optional] 
 **source_compute** | **str**| The source compute node of migration to filter.  | [optional] 
 **status** | **str**| The status of migration to filter.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **marker** | **str**| The UUID of the last-seen migration. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **changes_since** | **str**| Filters the response by a date and time stamp when the migration last changed. Those changed after the specified date and time stamp are returned.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-since&#x60;&#x60; must be earlier than or equal to the value of the &#x60;&#x60;changes-before&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **changes_before** | **str**| Filters the response by a date and time stamp when the migration last changed. Those migrations that changed before or equal to the specified date and time stamp are returned.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-before&#x60;&#x60; must be later than or equal to the value of the &#x60;&#x60;changes-since&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **user_id** | **str**| Filter the migrations by the given user ID.  | [optional] 
 **project_id** | **str**| Filter the migrations by the given project ID.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


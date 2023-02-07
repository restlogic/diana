# swagger_client.ServersApi

All URIs are relative to *https://host*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v21_servers_detail_get**](ServersApi.md#v21_servers_detail_get) | **GET** /v2.1/servers/detail | 
[**v21_servers_get**](ServersApi.md#v21_servers_get) | **GET** /v2.1/servers | 
[**v21_servers_post**](ServersApi.md#v21_servers_post) | **POST** /v2.1/servers | 
[**v21_servers_server_id_delete**](ServersApi.md#v21_servers_server_id_delete) | **DELETE** /v2.1/servers/{server_id} | 
[**v21_servers_server_id_get**](ServersApi.md#v21_servers_server_id_get) | **GET** /v2.1/servers/{server_id} | 
[**v21_servers_server_id_put**](ServersApi.md#v21_servers_server_id_put) | **PUT** /v2.1/servers/{server_id} | 


# **v21_servers_detail_get**
> v21_servers_detail_get(access_ip_v4=access_ip_v4, access_ip_v6=access_ip_v6, all_tenants=all_tenants, auto_disk_config=auto_disk_config, availability_zone=availability_zone, changes_since=changes_since, config_drive=config_drive, created_at=created_at, deleted=deleted, description=description, flavor=flavor, host=host, hostname=hostname, image=image, ip=ip, ip6=ip6, kernel_id=kernel_id, key_name=key_name, launch_index=launch_index, launched_at=launched_at, limit=limit, locked_by=locked_by, marker=marker, name=name, node=node, power_state=power_state, progress=progress, project_id=project_id, ramdisk_id=ramdisk_id, reservation_id=reservation_id, root_device_name=root_device_name, soft_deleted=soft_deleted, sort_dir=sort_dir, sort_key=sort_key, status=status, task_state=task_state, terminated_at=terminated_at, user_id=user_id, uuid=uuid, vm_state=vm_state, not_tags=not_tags, not_tags_any=not_tags_any, tags=tags, tags_any=tags_any, changes_before=changes_before, locked=locked)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
access_ip_v4 = 'access_ip_v4_example' # str | Filter server list result by IPv4 address that should be used to access the server.  (optional)
access_ip_v6 = 'access_ip_v6_example' # str | Filter server list result by IPv6 address that should be used to access the server.  (optional)
all_tenants = true # bool | Specify the ``all_tenants`` query parameter to list all instances for all projects. By default this is only allowed by administrators. If this parameter is specified without a value, the value defaults to ``True``. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False``. (They are case-insensitive.)  (optional)
auto_disk_config = 'auto_disk_config_example' # str | Filter the server list result by the ``disk_config`` setting of the server, Valid values are:  - ``AUTO`` - ``MANUAL``  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
availability_zone = 'availability_zone_example' # str | Filter the server list result by server availability zone.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
changes_since = 'changes_since_example' # str | Filters the response by a date and time stamp when the server last changed status. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400.  (optional)
config_drive = 'config_drive_example' # str | Filter the server list result by the config drive setting of the server.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
created_at = 'created_at_example' # str | Filter the server list result by a date and time stamp when server was created.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
deleted = true # bool | Show deleted items only. In some circumstances deleted items will still be accessible via the backend database, however there is no contract on how long, so this parameter should be used with caution. ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True`` (case-insensitive). Other than them are treated as ``False``.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
description = 'description_example' # str | Filter the server list result by description.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  .. note::     ``display_description`` can also be requested which is alias of    ``description`` but that is not recommended to use as that will    be removed in future.  (optional)
flavor = 'flavor_example' # str | Filters the response by a flavor, as a UUID. A flavor is a combination of memory, disk size, and CPUs.  (optional)
host = 'host_example' # str | Filter the server list result by the host name of compute node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
hostname = 'hostname_example' # str | Filter the server list result by the host name of server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
image = 'image_example' # str | Filters the response by an image, as a UUID.  .. note::     'image_ref' can also be requested which is alias of 'image'    but that is not recommended to use as that will be removed in future.  (optional)
ip = 'ip_example' # str | An IPv4 address to filter results by.  (optional)
ip6 = 'ip6_example' # str | An IPv6 address to filter results by.  Up to microversion 2.4, this parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored. Starting from microversion 2.5, this parameter is valid for no-admin users as well as administrators.  (optional)
kernel_id = 'kernel_id_example' # str | Filter the server list result by the UUID of the kernel image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
key_name = 'key_name_example' # str | Filter the server list result by keypair name.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
launch_index = 56 # int | Filter the server list result by the sequence in which the servers were launched.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
launched_at = 'launched_at_example' # str | Filter the server list result by a date and time stamp when the instance was launched. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
locked_by = 'locked_by_example' # str | Filter the server list result by who locked the server, possible value could be ``admin`` or ``owner``.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
name = 'name_example' # str | Filters the response by a server name, as a string.  You can use regular expressions in the query. For example, the ``?name=bob`` regular expression returns both bob and bobb. If you must match on only bob, you can use a regular expression that matches the syntax of the underlying database server that is implemented for Compute, such as MySQL or PostgreSQL.  .. note::     'display_name' can also be requested which is alias of 'name'    but that is not recommended to use as that will be removed in future.  (optional)
node = 'node_example' # str | Filter the server list result by the node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
power_state = 56 # int | Filter the server list result by server power state.  Possible values are integer values that is mapped as::    0: NOSTATE   1: RUNNING   3: PAUSED   4: SHUTDOWN   6: CRASHED   7: SUSPENDED  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
progress = 56 # int | Filter the server list result by the progress of the server. The value could be from 0 to 100 as integer.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
project_id = 'project_id_example' # str | Filter the list of servers by the given project ID.  This filter only works when the ``all_tenants`` filter is also specified.  .. note::     'tenant_id' can also be requested which is alias of 'project_id'    but that is not recommended to use as that will be removed in future.  (optional)
ramdisk_id = 'ramdisk_id_example' # str | Filter the server list result by the UUID of the ramdisk image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
reservation_id = 'reservation_id_example' # str | A reservation id as returned by a servers multiple create call.  (optional)
root_device_name = 'root_device_name_example' # str | Filter the server list result by the root device name of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
soft_deleted = true # bool | Filter the server list by ``SOFT_DELETED`` status. This parameter is only valid when the ``deleted=True`` filter parameter is specified.  (optional)
sort_dir = 'sort_dir_example' # str | Sort direction. A valid value is ``asc`` (ascending) or ``desc`` (descending). Default is ``desc``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server ``sort_key`` attribute.  (optional)
sort_key = 'sort_key_example' # str | Sorts by a server attribute. Default attribute is ``created_at``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server ``sort_key`` attribute. The sort keys are limited to:  - ``access_ip_v4`` - ``access_ip_v6`` - ``auto_disk_config`` - ``availability_zone`` - ``config_drive`` - ``created_at`` - ``display_description`` - ``display_name`` - ``host`` - ``hostname`` - ``image_ref`` - ``instance_type_id`` - ``kernel_id`` - ``key_name`` - ``launch_index`` - ``launched_at`` - ``locked`` (New in version 2.73) - ``locked_by`` - ``node`` - ``power_state`` - ``progress`` - ``project_id`` - ``ramdisk_id`` - ``root_device_name`` - ``task_state`` - ``terminated_at`` - ``updated_at`` - ``user_id`` - ``uuid`` - ``vm_state``  ``host`` and ``node`` are only allowed for admin. If non-admin users specify them, a 403 error is returned.  (optional)
status = 'status_example' # str | Filters the response by a server status, as a string. For example, ``ACTIVE``.  Up to microversion 2.37, an empty list is returned if an invalid status is specified. Starting from microversion 2.38, a 400 error is returned in that case.  (optional)
task_state = 'task_state_example' # str | Filter the server list result by task state.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
terminated_at = 'terminated_at_example' # str | Filter the server list result by a date and time stamp when instance was terminated. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
user_id = 'user_id_example' # str | Filter the list of servers by the given user ID.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
uuid = 'uuid_example' # str | Filter the server list result by the UUID of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
vm_state = 'vm_state_example' # str | Filter the server list result by vm state.  The value could be:  - ``ACTIVE`` - ``BUILDING`` - ``DELETED`` - ``ERROR`` - ``PAUSED`` - ``RESCUED`` - ``RESIZED`` - ``SHELVED`` - ``SHELVED_OFFLOADED`` - ``SOFT_DELETED`` - ``STOPPED`` - ``SUSPENDED``  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
not_tags = 'not_tags_example' # str | A list of tags to filter the server list by. Servers that don't match all tags in this list will be returned. Boolean expression in this case is 'NOT (t1 AND t2)'. Tags in query must be separated by comma.  (optional)
not_tags_any = 'not_tags_any_example' # str | A list of tags to filter the server list by. Servers that don't match any tags in this list will be returned. Boolean expression in this case is 'NOT (t1 OR t2)'. Tags in query must be separated by comma.  (optional)
tags = 'tags_example' # str | A list of tags to filter the server list by. Servers that match all tags in this list will be returned. Boolean expression in this case is 't1 AND t2'. Tags in query must be separated by comma.  (optional)
tags_any = 'tags_any_example' # str | A list of tags to filter the server list by. Servers that match any tag in this list will be returned. Boolean expression in this case is 't1 OR t2'. Tags in query must be separated by comma.  (optional)
changes_before = 'changes_before_example' # str | Filters the response by a date and time stamp when the server last changed. Those servers that changed before or equal to the specified date and time stamp are returned. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400.  (optional)
locked = true # bool | Specify the ``locked`` query parameter to list all locked or unlocked instances. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False``. (They are case-insensitive.) Any other value provided will be considered invalid.  (optional)

try:
    api_instance.v21_servers_detail_get(access_ip_v4=access_ip_v4, access_ip_v6=access_ip_v6, all_tenants=all_tenants, auto_disk_config=auto_disk_config, availability_zone=availability_zone, changes_since=changes_since, config_drive=config_drive, created_at=created_at, deleted=deleted, description=description, flavor=flavor, host=host, hostname=hostname, image=image, ip=ip, ip6=ip6, kernel_id=kernel_id, key_name=key_name, launch_index=launch_index, launched_at=launched_at, limit=limit, locked_by=locked_by, marker=marker, name=name, node=node, power_state=power_state, progress=progress, project_id=project_id, ramdisk_id=ramdisk_id, reservation_id=reservation_id, root_device_name=root_device_name, soft_deleted=soft_deleted, sort_dir=sort_dir, sort_key=sort_key, status=status, task_state=task_state, terminated_at=terminated_at, user_id=user_id, uuid=uuid, vm_state=vm_state, not_tags=not_tags, not_tags_any=not_tags_any, tags=tags, tags_any=tags_any, changes_before=changes_before, locked=locked)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_ip_v4** | **str**| Filter server list result by IPv4 address that should be used to access the server.  | [optional] 
 **access_ip_v6** | **str**| Filter server list result by IPv6 address that should be used to access the server.  | [optional] 
 **all_tenants** | **bool**| Specify the &#x60;&#x60;all_tenants&#x60;&#x60; query parameter to list all instances for all projects. By default this is only allowed by administrators. If this parameter is specified without a value, the value defaults to &#x60;&#x60;True&#x60;&#x60;. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60;. (They are case-insensitive.)  | [optional] 
 **auto_disk_config** | **str**| Filter the server list result by the &#x60;&#x60;disk_config&#x60;&#x60; setting of the server, Valid values are:  - &#x60;&#x60;AUTO&#x60;&#x60; - &#x60;&#x60;MANUAL&#x60;&#x60;  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **availability_zone** | **str**| Filter the server list result by server availability zone.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **changes_since** | **str**| Filters the response by a date and time stamp when the server last changed status. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-since&#x60;&#x60; must be earlier than or equal to the value of the &#x60;&#x60;changes-before&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **config_drive** | **str**| Filter the server list result by the config drive setting of the server.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **created_at** | **str**| Filter the server list result by a date and time stamp when server was created.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **deleted** | **bool**| Show deleted items only. In some circumstances deleted items will still be accessible via the backend database, however there is no contract on how long, so this parameter should be used with caution. &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60; (case-insensitive). Other than them are treated as &#x60;&#x60;False&#x60;&#x60;.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **description** | **str**| Filter the server list result by description.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  .. note::     &#x60;&#x60;display_description&#x60;&#x60; can also be requested which is alias of    &#x60;&#x60;description&#x60;&#x60; but that is not recommended to use as that will    be removed in future.  | [optional] 
 **flavor** | **str**| Filters the response by a flavor, as a UUID. A flavor is a combination of memory, disk size, and CPUs.  | [optional] 
 **host** | **str**| Filter the server list result by the host name of compute node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **hostname** | **str**| Filter the server list result by the host name of server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **image** | **str**| Filters the response by an image, as a UUID.  .. note::     &#39;image_ref&#39; can also be requested which is alias of &#39;image&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **ip** | **str**| An IPv4 address to filter results by.  | [optional] 
 **ip6** | **str**| An IPv6 address to filter results by.  Up to microversion 2.4, this parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored. Starting from microversion 2.5, this parameter is valid for no-admin users as well as administrators.  | [optional] 
 **kernel_id** | **str**| Filter the server list result by the UUID of the kernel image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **key_name** | **str**| Filter the server list result by keypair name.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **launch_index** | **int**| Filter the server list result by the sequence in which the servers were launched.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **launched_at** | **str**| Filter the server list result by a date and time stamp when the instance was launched. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **locked_by** | **str**| Filter the server list result by who locked the server, possible value could be &#x60;&#x60;admin&#x60;&#x60; or &#x60;&#x60;owner&#x60;&#x60;.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **name** | **str**| Filters the response by a server name, as a string.  You can use regular expressions in the query. For example, the &#x60;&#x60;?name&#x3D;bob&#x60;&#x60; regular expression returns both bob and bobb. If you must match on only bob, you can use a regular expression that matches the syntax of the underlying database server that is implemented for Compute, such as MySQL or PostgreSQL.  .. note::     &#39;display_name&#39; can also be requested which is alias of &#39;name&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **node** | **str**| Filter the server list result by the node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **power_state** | **int**| Filter the server list result by server power state.  Possible values are integer values that is mapped as::    0: NOSTATE   1: RUNNING   3: PAUSED   4: SHUTDOWN   6: CRASHED   7: SUSPENDED  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **progress** | **int**| Filter the server list result by the progress of the server. The value could be from 0 to 100 as integer.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **project_id** | **str**| Filter the list of servers by the given project ID.  This filter only works when the &#x60;&#x60;all_tenants&#x60;&#x60; filter is also specified.  .. note::     &#39;tenant_id&#39; can also be requested which is alias of &#39;project_id&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **ramdisk_id** | **str**| Filter the server list result by the UUID of the ramdisk image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **reservation_id** | **str**| A reservation id as returned by a servers multiple create call.  | [optional] 
 **root_device_name** | **str**| Filter the server list result by the root device name of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **soft_deleted** | **bool**| Filter the server list by &#x60;&#x60;SOFT_DELETED&#x60;&#x60; status. This parameter is only valid when the &#x60;&#x60;deleted&#x3D;True&#x60;&#x60; filter parameter is specified.  | [optional] 
 **sort_dir** | **str**| Sort direction. A valid value is &#x60;&#x60;asc&#x60;&#x60; (ascending) or &#x60;&#x60;desc&#x60;&#x60; (descending). Default is &#x60;&#x60;desc&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server &#x60;&#x60;sort_key&#x60;&#x60; attribute.  | [optional] 
 **sort_key** | **str**| Sorts by a server attribute. Default attribute is &#x60;&#x60;created_at&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server &#x60;&#x60;sort_key&#x60;&#x60; attribute. The sort keys are limited to:  - &#x60;&#x60;access_ip_v4&#x60;&#x60; - &#x60;&#x60;access_ip_v6&#x60;&#x60; - &#x60;&#x60;auto_disk_config&#x60;&#x60; - &#x60;&#x60;availability_zone&#x60;&#x60; - &#x60;&#x60;config_drive&#x60;&#x60; - &#x60;&#x60;created_at&#x60;&#x60; - &#x60;&#x60;display_description&#x60;&#x60; - &#x60;&#x60;display_name&#x60;&#x60; - &#x60;&#x60;host&#x60;&#x60; - &#x60;&#x60;hostname&#x60;&#x60; - &#x60;&#x60;image_ref&#x60;&#x60; - &#x60;&#x60;instance_type_id&#x60;&#x60; - &#x60;&#x60;kernel_id&#x60;&#x60; - &#x60;&#x60;key_name&#x60;&#x60; - &#x60;&#x60;launch_index&#x60;&#x60; - &#x60;&#x60;launched_at&#x60;&#x60; - &#x60;&#x60;locked&#x60;&#x60; (New in version 2.73) - &#x60;&#x60;locked_by&#x60;&#x60; - &#x60;&#x60;node&#x60;&#x60; - &#x60;&#x60;power_state&#x60;&#x60; - &#x60;&#x60;progress&#x60;&#x60; - &#x60;&#x60;project_id&#x60;&#x60; - &#x60;&#x60;ramdisk_id&#x60;&#x60; - &#x60;&#x60;root_device_name&#x60;&#x60; - &#x60;&#x60;task_state&#x60;&#x60; - &#x60;&#x60;terminated_at&#x60;&#x60; - &#x60;&#x60;updated_at&#x60;&#x60; - &#x60;&#x60;user_id&#x60;&#x60; - &#x60;&#x60;uuid&#x60;&#x60; - &#x60;&#x60;vm_state&#x60;&#x60;  &#x60;&#x60;host&#x60;&#x60; and &#x60;&#x60;node&#x60;&#x60; are only allowed for admin. If non-admin users specify them, a 403 error is returned.  | [optional] 
 **status** | **str**| Filters the response by a server status, as a string. For example, &#x60;&#x60;ACTIVE&#x60;&#x60;.  Up to microversion 2.37, an empty list is returned if an invalid status is specified. Starting from microversion 2.38, a 400 error is returned in that case.  | [optional] 
 **task_state** | **str**| Filter the server list result by task state.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **terminated_at** | **str**| Filter the server list result by a date and time stamp when instance was terminated. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **user_id** | **str**| Filter the list of servers by the given user ID.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **uuid** | **str**| Filter the server list result by the UUID of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **vm_state** | **str**| Filter the server list result by vm state.  The value could be:  - &#x60;&#x60;ACTIVE&#x60;&#x60; - &#x60;&#x60;BUILDING&#x60;&#x60; - &#x60;&#x60;DELETED&#x60;&#x60; - &#x60;&#x60;ERROR&#x60;&#x60; - &#x60;&#x60;PAUSED&#x60;&#x60; - &#x60;&#x60;RESCUED&#x60;&#x60; - &#x60;&#x60;RESIZED&#x60;&#x60; - &#x60;&#x60;SHELVED&#x60;&#x60; - &#x60;&#x60;SHELVED_OFFLOADED&#x60;&#x60; - &#x60;&#x60;SOFT_DELETED&#x60;&#x60; - &#x60;&#x60;STOPPED&#x60;&#x60; - &#x60;&#x60;SUSPENDED&#x60;&#x60;  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **not_tags** | **str**| A list of tags to filter the server list by. Servers that don&#39;t match all tags in this list will be returned. Boolean expression in this case is &#39;NOT (t1 AND t2)&#39;. Tags in query must be separated by comma.  | [optional] 
 **not_tags_any** | **str**| A list of tags to filter the server list by. Servers that don&#39;t match any tags in this list will be returned. Boolean expression in this case is &#39;NOT (t1 OR t2)&#39;. Tags in query must be separated by comma.  | [optional] 
 **tags** | **str**| A list of tags to filter the server list by. Servers that match all tags in this list will be returned. Boolean expression in this case is &#39;t1 AND t2&#39;. Tags in query must be separated by comma.  | [optional] 
 **tags_any** | **str**| A list of tags to filter the server list by. Servers that match any tag in this list will be returned. Boolean expression in this case is &#39;t1 OR t2&#39;. Tags in query must be separated by comma.  | [optional] 
 **changes_before** | **str**| Filters the response by a date and time stamp when the server last changed. Those servers that changed before or equal to the specified date and time stamp are returned. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-before&#x60;&#x60; must be later than or equal to the value of the &#x60;&#x60;changes-since&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **locked** | **bool**| Specify the &#x60;&#x60;locked&#x60;&#x60; query parameter to list all locked or unlocked instances. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60;. (They are case-insensitive.) Any other value provided will be considered invalid.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_get**
> v21_servers_get(access_ip_v4=access_ip_v4, access_ip_v6=access_ip_v6, all_tenants=all_tenants, auto_disk_config=auto_disk_config, availability_zone=availability_zone, changes_since=changes_since, config_drive=config_drive, created_at=created_at, deleted=deleted, description=description, flavor=flavor, host=host, hostname=hostname, image=image, ip=ip, ip6=ip6, kernel_id=kernel_id, key_name=key_name, launch_index=launch_index, launched_at=launched_at, limit=limit, locked_by=locked_by, marker=marker, name=name, node=node, power_state=power_state, progress=progress, project_id=project_id, ramdisk_id=ramdisk_id, reservation_id=reservation_id, root_device_name=root_device_name, soft_deleted=soft_deleted, sort_dir=sort_dir, sort_key=sort_key, status=status, task_state=task_state, terminated_at=terminated_at, user_id=user_id, uuid=uuid, vm_state=vm_state, not_tags=not_tags, not_tags_any=not_tags_any, tags=tags, tags_any=tags_any, changes_before=changes_before, locked=locked)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
access_ip_v4 = 'access_ip_v4_example' # str | Filter server list result by IPv4 address that should be used to access the server.  (optional)
access_ip_v6 = 'access_ip_v6_example' # str | Filter server list result by IPv6 address that should be used to access the server.  (optional)
all_tenants = true # bool | Specify the ``all_tenants`` query parameter to list all instances for all projects. By default this is only allowed by administrators. If this parameter is specified without a value, the value defaults to ``True``. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False``. (They are case-insensitive.)  (optional)
auto_disk_config = 'auto_disk_config_example' # str | Filter the server list result by the ``disk_config`` setting of the server, Valid values are:  - ``AUTO`` - ``MANUAL``  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
availability_zone = 'availability_zone_example' # str | Filter the server list result by server availability zone.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
changes_since = 'changes_since_example' # str | Filters the response by a date and time stamp when the server last changed status. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-since`` must be earlier than or equal to the value of the ``changes-before`` otherwise API will return 400.  (optional)
config_drive = 'config_drive_example' # str | Filter the server list result by the config drive setting of the server.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
created_at = 'created_at_example' # str | Filter the server list result by a date and time stamp when server was created.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
deleted = true # bool | Show deleted items only. In some circumstances deleted items will still be accessible via the backend database, however there is no contract on how long, so this parameter should be used with caution. ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True`` (case-insensitive). Other than them are treated as ``False``.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
description = 'description_example' # str | Filter the server list result by description.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  .. note::     ``display_description`` can also be requested which is alias of    ``description`` but that is not recommended to use as that will    be removed in future.  (optional)
flavor = 'flavor_example' # str | Filters the response by a flavor, as a UUID. A flavor is a combination of memory, disk size, and CPUs.  (optional)
host = 'host_example' # str | Filter the server list result by the host name of compute node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
hostname = 'hostname_example' # str | Filter the server list result by the host name of server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
image = 'image_example' # str | Filters the response by an image, as a UUID.  .. note::     'image_ref' can also be requested which is alias of 'image'    but that is not recommended to use as that will be removed in future.  (optional)
ip = 'ip_example' # str | An IPv4 address to filter results by.  (optional)
ip6 = 'ip6_example' # str | An IPv6 address to filter results by.  Up to microversion 2.4, this parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored. Starting from microversion 2.5, this parameter is valid for no-admin users as well as administrators.  (optional)
kernel_id = 'kernel_id_example' # str | Filter the server list result by the UUID of the kernel image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
key_name = 'key_name_example' # str | Filter the server list result by keypair name.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
launch_index = 56 # int | Filter the server list result by the sequence in which the servers were launched.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
launched_at = 'launched_at_example' # str | Filter the server list result by a date and time stamp when the instance was launched. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
limit = 56 # int | Requests a page size of items. Returns a number of items up to a limit value. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
locked_by = 'locked_by_example' # str | Filter the server list result by who locked the server, possible value could be ``admin`` or ``owner``.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
marker = 'marker_example' # str | The ID of the last-seen item. Use the ``limit`` parameter to make an initial limited request and use the ID of the last-seen item from the response as the ``marker`` parameter value in a subsequent limited request.  (optional)
name = 'name_example' # str | Filters the response by a server name, as a string.  You can use regular expressions in the query. For example, the ``?name=bob`` regular expression returns both bob and bobb. If you must match on only bob, you can use a regular expression that matches the syntax of the underlying database server that is implemented for Compute, such as MySQL or PostgreSQL.  .. note::     'display_name' can also be requested which is alias of 'name'    but that is not recommended to use as that will be removed in future.  (optional)
node = 'node_example' # str | Filter the server list result by the node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
power_state = 56 # int | Filter the server list result by server power state.  Possible values are integer values that is mapped as::    0: NOSTATE   1: RUNNING   3: PAUSED   4: SHUTDOWN   6: CRASHED   7: SUSPENDED  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
progress = 56 # int | Filter the server list result by the progress of the server. The value could be from 0 to 100 as integer.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
project_id = 'project_id_example' # str | Filter the list of servers by the given project ID.  This filter only works when the ``all_tenants`` filter is also specified.  .. note::     'tenant_id' can also be requested which is alias of 'project_id'    but that is not recommended to use as that will be removed in future.  (optional)
ramdisk_id = 'ramdisk_id_example' # str | Filter the server list result by the UUID of the ramdisk image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
reservation_id = 'reservation_id_example' # str | A reservation id as returned by a servers multiple create call.  (optional)
root_device_name = 'root_device_name_example' # str | Filter the server list result by the root device name of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
soft_deleted = true # bool | Filter the server list by ``SOFT_DELETED`` status. This parameter is only valid when the ``deleted=True`` filter parameter is specified.  (optional)
sort_dir = 'sort_dir_example' # str | Sort direction. A valid value is ``asc`` (ascending) or ``desc`` (descending). Default is ``desc``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server ``sort_key`` attribute.  (optional)
sort_key = 'sort_key_example' # str | Sorts by a server attribute. Default attribute is ``created_at``. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server ``sort_key`` attribute. The sort keys are limited to:  - ``access_ip_v4`` - ``access_ip_v6`` - ``auto_disk_config`` - ``availability_zone`` - ``config_drive`` - ``created_at`` - ``display_description`` - ``display_name`` - ``host`` - ``hostname`` - ``image_ref`` - ``instance_type_id`` - ``kernel_id`` - ``key_name`` - ``launch_index`` - ``launched_at`` - ``locked`` (New in version 2.73) - ``locked_by`` - ``node`` - ``power_state`` - ``progress`` - ``project_id`` - ``ramdisk_id`` - ``root_device_name`` - ``task_state`` - ``terminated_at`` - ``updated_at`` - ``user_id`` - ``uuid`` - ``vm_state``  ``host`` and ``node`` are only allowed for admin. If non-admin users specify them, a 403 error is returned.  (optional)
status = 'status_example' # str | Filters the response by a server status, as a string. For example, ``ACTIVE``.  Up to microversion 2.37, an empty list is returned if an invalid status is specified. Starting from microversion 2.38, a 400 error is returned in that case.  (optional)
task_state = 'task_state_example' # str | Filter the server list result by task state.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
terminated_at = 'terminated_at_example' # str | Filter the server list result by a date and time stamp when instance was terminated. The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
user_id = 'user_id_example' # str | Filter the list of servers by the given user ID.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
uuid = 'uuid_example' # str | Filter the server list result by the UUID of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  (optional)
vm_state = 'vm_state_example' # str | Filter the server list result by vm state.  The value could be:  - ``ACTIVE`` - ``BUILDING`` - ``DELETED`` - ``ERROR`` - ``PAUSED`` - ``RESCUED`` - ``RESIZED`` - ``SHELVED`` - ``SHELVED_OFFLOADED`` - ``SOFT_DELETED`` - ``STOPPED`` - ``SUSPENDED``  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  (optional)
not_tags = 'not_tags_example' # str | A list of tags to filter the server list by. Servers that don't match all tags in this list will be returned. Boolean expression in this case is 'NOT (t1 AND t2)'. Tags in query must be separated by comma.  (optional)
not_tags_any = 'not_tags_any_example' # str | A list of tags to filter the server list by. Servers that don't match any tags in this list will be returned. Boolean expression in this case is 'NOT (t1 OR t2)'. Tags in query must be separated by comma.  (optional)
tags = 'tags_example' # str | A list of tags to filter the server list by. Servers that match all tags in this list will be returned. Boolean expression in this case is 't1 AND t2'. Tags in query must be separated by comma.  (optional)
tags_any = 'tags_any_example' # str | A list of tags to filter the server list by. Servers that match any tag in this list will be returned. Boolean expression in this case is 't1 OR t2'. Tags in query must be separated by comma.  (optional)
changes_before = 'changes_before_example' # str | Filters the response by a date and time stamp when the server last changed. Those servers that changed before or equal to the specified date and time stamp are returned. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The ``±hh:mm`` value, if included, returns the time zone as an offset from UTC. For example, ``2015-08-27T09:49:58-05:00``. If you omit the time zone, the UTC time zone is assumed. When both ``changes-since`` and ``changes-before`` are specified, the value of the ``changes-before`` must be later than or equal to the value of the ``changes-since`` otherwise API will return 400.  (optional)
locked = true # bool | Specify the ``locked`` query parameter to list all locked or unlocked instances. If the value is specified, ``1``, ``t``, ``true``, ``on``, ``y`` and ``yes`` are treated as ``True``. ``0``, ``f``, ``false``, ``off``, ``n`` and ``no`` are treated as ``False``. (They are case-insensitive.) Any other value provided will be considered invalid.  (optional)

try:
    api_instance.v21_servers_get(access_ip_v4=access_ip_v4, access_ip_v6=access_ip_v6, all_tenants=all_tenants, auto_disk_config=auto_disk_config, availability_zone=availability_zone, changes_since=changes_since, config_drive=config_drive, created_at=created_at, deleted=deleted, description=description, flavor=flavor, host=host, hostname=hostname, image=image, ip=ip, ip6=ip6, kernel_id=kernel_id, key_name=key_name, launch_index=launch_index, launched_at=launched_at, limit=limit, locked_by=locked_by, marker=marker, name=name, node=node, power_state=power_state, progress=progress, project_id=project_id, ramdisk_id=ramdisk_id, reservation_id=reservation_id, root_device_name=root_device_name, soft_deleted=soft_deleted, sort_dir=sort_dir, sort_key=sort_key, status=status, task_state=task_state, terminated_at=terminated_at, user_id=user_id, uuid=uuid, vm_state=vm_state, not_tags=not_tags, not_tags_any=not_tags_any, tags=tags, tags_any=tags_any, changes_before=changes_before, locked=locked)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_ip_v4** | **str**| Filter server list result by IPv4 address that should be used to access the server.  | [optional] 
 **access_ip_v6** | **str**| Filter server list result by IPv6 address that should be used to access the server.  | [optional] 
 **all_tenants** | **bool**| Specify the &#x60;&#x60;all_tenants&#x60;&#x60; query parameter to list all instances for all projects. By default this is only allowed by administrators. If this parameter is specified without a value, the value defaults to &#x60;&#x60;True&#x60;&#x60;. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60;. (They are case-insensitive.)  | [optional] 
 **auto_disk_config** | **str**| Filter the server list result by the &#x60;&#x60;disk_config&#x60;&#x60; setting of the server, Valid values are:  - &#x60;&#x60;AUTO&#x60;&#x60; - &#x60;&#x60;MANUAL&#x60;&#x60;  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **availability_zone** | **str**| Filter the server list result by server availability zone.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **changes_since** | **str**| Filters the response by a date and time stamp when the server last changed status. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-since&#x60;&#x60; must be earlier than or equal to the value of the &#x60;&#x60;changes-before&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **config_drive** | **str**| Filter the server list result by the config drive setting of the server.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **created_at** | **str**| Filter the server list result by a date and time stamp when server was created.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **deleted** | **bool**| Show deleted items only. In some circumstances deleted items will still be accessible via the backend database, however there is no contract on how long, so this parameter should be used with caution. &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60; (case-insensitive). Other than them are treated as &#x60;&#x60;False&#x60;&#x60;.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **description** | **str**| Filter the server list result by description.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  .. note::     &#x60;&#x60;display_description&#x60;&#x60; can also be requested which is alias of    &#x60;&#x60;description&#x60;&#x60; but that is not recommended to use as that will    be removed in future.  | [optional] 
 **flavor** | **str**| Filters the response by a flavor, as a UUID. A flavor is a combination of memory, disk size, and CPUs.  | [optional] 
 **host** | **str**| Filter the server list result by the host name of compute node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **hostname** | **str**| Filter the server list result by the host name of server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **image** | **str**| Filters the response by an image, as a UUID.  .. note::     &#39;image_ref&#39; can also be requested which is alias of &#39;image&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **ip** | **str**| An IPv4 address to filter results by.  | [optional] 
 **ip6** | **str**| An IPv6 address to filter results by.  Up to microversion 2.4, this parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored. Starting from microversion 2.5, this parameter is valid for no-admin users as well as administrators.  | [optional] 
 **kernel_id** | **str**| Filter the server list result by the UUID of the kernel image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **key_name** | **str**| Filter the server list result by keypair name.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **launch_index** | **int**| Filter the server list result by the sequence in which the servers were launched.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **launched_at** | **str**| Filter the server list result by a date and time stamp when the instance was launched. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **limit** | **int**| Requests a page size of items. Returns a number of items up to a limit value. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **locked_by** | **str**| Filter the server list result by who locked the server, possible value could be &#x60;&#x60;admin&#x60;&#x60; or &#x60;&#x60;owner&#x60;&#x60;.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **marker** | **str**| The ID of the last-seen item. Use the &#x60;&#x60;limit&#x60;&#x60; parameter to make an initial limited request and use the ID of the last-seen item from the response as the &#x60;&#x60;marker&#x60;&#x60; parameter value in a subsequent limited request.  | [optional] 
 **name** | **str**| Filters the response by a server name, as a string.  You can use regular expressions in the query. For example, the &#x60;&#x60;?name&#x3D;bob&#x60;&#x60; regular expression returns both bob and bobb. If you must match on only bob, you can use a regular expression that matches the syntax of the underlying database server that is implemented for Compute, such as MySQL or PostgreSQL.  .. note::     &#39;display_name&#39; can also be requested which is alias of &#39;name&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **node** | **str**| Filter the server list result by the node.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **power_state** | **int**| Filter the server list result by server power state.  Possible values are integer values that is mapped as::    0: NOSTATE   1: RUNNING   3: PAUSED   4: SHUTDOWN   6: CRASHED   7: SUSPENDED  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **progress** | **int**| Filter the server list result by the progress of the server. The value could be from 0 to 100 as integer.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **project_id** | **str**| Filter the list of servers by the given project ID.  This filter only works when the &#x60;&#x60;all_tenants&#x60;&#x60; filter is also specified.  .. note::     &#39;tenant_id&#39; can also be requested which is alias of &#39;project_id&#39;    but that is not recommended to use as that will be removed in future.  | [optional] 
 **ramdisk_id** | **str**| Filter the server list result by the UUID of the ramdisk image when using an AMI.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **reservation_id** | **str**| A reservation id as returned by a servers multiple create call.  | [optional] 
 **root_device_name** | **str**| Filter the server list result by the root device name of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **soft_deleted** | **bool**| Filter the server list by &#x60;&#x60;SOFT_DELETED&#x60;&#x60; status. This parameter is only valid when the &#x60;&#x60;deleted&#x3D;True&#x60;&#x60; filter parameter is specified.  | [optional] 
 **sort_dir** | **str**| Sort direction. A valid value is &#x60;&#x60;asc&#x60;&#x60; (ascending) or &#x60;&#x60;desc&#x60;&#x60; (descending). Default is &#x60;&#x60;desc&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server &#x60;&#x60;sort_key&#x60;&#x60; attribute.  | [optional] 
 **sort_key** | **str**| Sorts by a server attribute. Default attribute is &#x60;&#x60;created_at&#x60;&#x60;. You can specify multiple pairs of sort key and sort direction query parameters. If you omit the sort direction in a pair, the API uses the natural sorting direction of the server &#x60;&#x60;sort_key&#x60;&#x60; attribute. The sort keys are limited to:  - &#x60;&#x60;access_ip_v4&#x60;&#x60; - &#x60;&#x60;access_ip_v6&#x60;&#x60; - &#x60;&#x60;auto_disk_config&#x60;&#x60; - &#x60;&#x60;availability_zone&#x60;&#x60; - &#x60;&#x60;config_drive&#x60;&#x60; - &#x60;&#x60;created_at&#x60;&#x60; - &#x60;&#x60;display_description&#x60;&#x60; - &#x60;&#x60;display_name&#x60;&#x60; - &#x60;&#x60;host&#x60;&#x60; - &#x60;&#x60;hostname&#x60;&#x60; - &#x60;&#x60;image_ref&#x60;&#x60; - &#x60;&#x60;instance_type_id&#x60;&#x60; - &#x60;&#x60;kernel_id&#x60;&#x60; - &#x60;&#x60;key_name&#x60;&#x60; - &#x60;&#x60;launch_index&#x60;&#x60; - &#x60;&#x60;launched_at&#x60;&#x60; - &#x60;&#x60;locked&#x60;&#x60; (New in version 2.73) - &#x60;&#x60;locked_by&#x60;&#x60; - &#x60;&#x60;node&#x60;&#x60; - &#x60;&#x60;power_state&#x60;&#x60; - &#x60;&#x60;progress&#x60;&#x60; - &#x60;&#x60;project_id&#x60;&#x60; - &#x60;&#x60;ramdisk_id&#x60;&#x60; - &#x60;&#x60;root_device_name&#x60;&#x60; - &#x60;&#x60;task_state&#x60;&#x60; - &#x60;&#x60;terminated_at&#x60;&#x60; - &#x60;&#x60;updated_at&#x60;&#x60; - &#x60;&#x60;user_id&#x60;&#x60; - &#x60;&#x60;uuid&#x60;&#x60; - &#x60;&#x60;vm_state&#x60;&#x60;  &#x60;&#x60;host&#x60;&#x60; and &#x60;&#x60;node&#x60;&#x60; are only allowed for admin. If non-admin users specify them, a 403 error is returned.  | [optional] 
 **status** | **str**| Filters the response by a server status, as a string. For example, &#x60;&#x60;ACTIVE&#x60;&#x60;.  Up to microversion 2.37, an empty list is returned if an invalid status is specified. Starting from microversion 2.38, a 400 error is returned in that case.  | [optional] 
 **task_state** | **str**| Filter the server list result by task state.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **terminated_at** | **str**| Filter the server list result by a date and time stamp when instance was terminated. The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **user_id** | **str**| Filter the list of servers by the given user ID.  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **uuid** | **str**| Filter the server list result by the UUID of the server.  This parameter is only valid when specified by administrators. If non-admin users specify this parameter, it is ignored.  | [optional] 
 **vm_state** | **str**| Filter the server list result by vm state.  The value could be:  - &#x60;&#x60;ACTIVE&#x60;&#x60; - &#x60;&#x60;BUILDING&#x60;&#x60; - &#x60;&#x60;DELETED&#x60;&#x60; - &#x60;&#x60;ERROR&#x60;&#x60; - &#x60;&#x60;PAUSED&#x60;&#x60; - &#x60;&#x60;RESCUED&#x60;&#x60; - &#x60;&#x60;RESIZED&#x60;&#x60; - &#x60;&#x60;SHELVED&#x60;&#x60; - &#x60;&#x60;SHELVED_OFFLOADED&#x60;&#x60; - &#x60;&#x60;SOFT_DELETED&#x60;&#x60; - &#x60;&#x60;STOPPED&#x60;&#x60; - &#x60;&#x60;SUSPENDED&#x60;&#x60;  This parameter is restricted to administrators until microversion 2.83. If non-admin users specify this parameter on a microversion less than 2.83, it will be ignored.  | [optional] 
 **not_tags** | **str**| A list of tags to filter the server list by. Servers that don&#39;t match all tags in this list will be returned. Boolean expression in this case is &#39;NOT (t1 AND t2)&#39;. Tags in query must be separated by comma.  | [optional] 
 **not_tags_any** | **str**| A list of tags to filter the server list by. Servers that don&#39;t match any tags in this list will be returned. Boolean expression in this case is &#39;NOT (t1 OR t2)&#39;. Tags in query must be separated by comma.  | [optional] 
 **tags** | **str**| A list of tags to filter the server list by. Servers that match all tags in this list will be returned. Boolean expression in this case is &#39;t1 AND t2&#39;. Tags in query must be separated by comma.  | [optional] 
 **tags_any** | **str**| A list of tags to filter the server list by. Servers that match any tag in this list will be returned. Boolean expression in this case is &#39;t1 OR t2&#39;. Tags in query must be separated by comma.  | [optional] 
 **changes_before** | **str**| Filters the response by a date and time stamp when the server last changed. Those servers that changed before or equal to the specified date and time stamp are returned. To help keep track of changes this may also return recently deleted servers.  The date and time stamp format is &#x60;ISO 8601 &lt;https://en.wikipedia.org/wiki/ISO_8601&gt;&#x60;_: ::     CCYY-MM-DDThh:mm:ss±hh:mm  The &#x60;&#x60;±hh:mm&#x60;&#x60; value, if included, returns the time zone as an offset from UTC. For example, &#x60;&#x60;2015-08-27T09:49:58-05:00&#x60;&#x60;. If you omit the time zone, the UTC time zone is assumed. When both &#x60;&#x60;changes-since&#x60;&#x60; and &#x60;&#x60;changes-before&#x60;&#x60; are specified, the value of the &#x60;&#x60;changes-before&#x60;&#x60; must be later than or equal to the value of the &#x60;&#x60;changes-since&#x60;&#x60; otherwise API will return 400.  | [optional] 
 **locked** | **bool**| Specify the &#x60;&#x60;locked&#x60;&#x60; query parameter to list all locked or unlocked instances. If the value is specified, &#x60;&#x60;1&#x60;&#x60;, &#x60;&#x60;t&#x60;&#x60;, &#x60;&#x60;true&#x60;&#x60;, &#x60;&#x60;on&#x60;&#x60;, &#x60;&#x60;y&#x60;&#x60; and &#x60;&#x60;yes&#x60;&#x60; are treated as &#x60;&#x60;True&#x60;&#x60;. &#x60;&#x60;0&#x60;&#x60;, &#x60;&#x60;f&#x60;&#x60;, &#x60;&#x60;false&#x60;&#x60;, &#x60;&#x60;off&#x60;&#x60;, &#x60;&#x60;n&#x60;&#x60; and &#x60;&#x60;no&#x60;&#x60; are treated as &#x60;&#x60;False&#x60;&#x60;. (They are case-insensitive.) Any other value provided will be considered invalid.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_post**
> v21_servers_post(server_create_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
server_create_req = swagger_client.ServerCreateReq() # ServerCreateReq | 

try:
    api_instance.v21_servers_post(server_create_req)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_create_req** | [**ServerCreateReq**](ServerCreateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v21_servers_server_id_delete**
> v21_servers_server_id_delete(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_delete(server_id)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_server_id_delete: %s\n" % e)
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

# **v21_servers_server_id_get**
> v21_servers_server_id_get(server_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
server_id = 'server_id_example' # str | The UUID of the server. 

try:
    api_instance.v21_servers_server_id_get(server_id)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_server_id_get: %s\n" % e)
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

# **v21_servers_server_id_put**
> v21_servers_server_id_put(server_id, server_update_req)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServersApi()
server_id = 'server_id_example' # str | The UUID of the server. 
server_update_req = swagger_client.ServerUpdateReq() # ServerUpdateReq | 

try:
    api_instance.v21_servers_server_id_put(server_id, server_update_req)
except ApiException as e:
    print("Exception when calling ServersApi->v21_servers_server_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The UUID of the server.  | 
 **server_update_req** | [**ServerUpdateReq**](ServerUpdateReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


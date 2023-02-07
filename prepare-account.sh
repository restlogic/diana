#!/bin/bash

# NOTICE: source init-rc credentials like /etc/kolla/admin-openrc.sh
PROJECT_NAME="test-project-1"
USER1_NAME="test-1"
USER2_NAME="test-2"

# openstack project show service
# +-------------+-------------------------------------------------+
# | Field       | Value                                           |
# +-------------+-------------------------------------------------+
# | description | None                                            |
# | domain_id   | default                                         |
# | enabled     | True                                            |
# | id          | baee9e0cc167465d8a3d0b9845ba716b                |
# | is_domain   | False                                           |
# | name        | service                                         |
# | options     | {}                                              |
# | parent_id   | default                                         |
# | tags        | ['default_stringneutron', 'default_stringnova'] |
# +-------------+-------------------------------------------------+

function create_project_if_not_exist()
{
	openstack project show $1
	if [[ $? -ne 0 ]]
	then
		openstack project create --domain default \
			--enable \
			$1
	fi
}
function create_user_if_not_exist()
{
	openstack user show $1
	if [[ $? -ne 0 ]]
	then
		openstack user create --domain default \
			--project ${PROJECT_NAME} \
			--password test \
			--enable \
			$1
	fi
}

create_project_if_not_exist ${PROJECT_NAME}

create_user_if_not_exist ${USER1_NAME}
create_user_if_not_exist ${USER2_NAME}

openstack role add --user ${USER1_NAME} --project ${PROJECT_NAME} member
openstack role add --user ${USER2_NAME} --project ${PROJECT_NAME} member
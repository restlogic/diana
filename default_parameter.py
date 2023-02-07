import pickle

# default_parameter example

default_parameter = {
    "nova": {
        # "AgentPostReq": {"agent": {"custom_type_parameter": "AgentpostreqAgent"}},
        "AgentpostreqAgent": {
            "architecture": "string_type_parameter",
            "hypervisor": "string_type_parameter",
            "md5hash": "string_type_parameter",
            "os": "string_type_parameter",
            "url": "string_type_parameter",
            "version": "string_type_parameter",
        },
        # "AggregatePostReq": {
        #     "aggregate": {"custom_type_parameter": "AggregatepostreqAggregate"}
        # },
        "AggregatepostreqAggregate": {
            "availability_zone": "string_type_parameter",
            "name": "string_type_parameter",
        },
        # "AttachInterfacesCreateNetIdReq": {
        #     "interface_attachment": {
        #         "custom_type_parameter": "AttachinterfacescreatenetIdreqInterfaceAttachment"
        #     }
        # },
        # "AttachVolumeToServerReq": {
        #     "volume_attachment": {
        #         "custom_type_parameter": "AttachvolumetoserverreqVolumeAttachment"
        #     }
        # },
        "AttachinterfacescreatenetIdreqInterfaceAttachment": {
            # "fixed_ips": {"custom_type_parameter": "list[FixedIp]"},
            "net_id": "string_type_parameter",
        },
        "AttachvolumetoserverreqVolumeAttachment": {
            "device": "string_type_parameter",
            "volume_id": "string_type_parameter",
        },
        "FixedIp": {"ip_address": "string_type_parameter"},
        "FlavorExtraSpecsCreateReq": {
            # "extra_specs": {
            #     "custom_type_parameter": "FlavorextraspecscreatereqExtraSpecs"
            # }
        },
        "FlavorextraspecscreatereqExtraSpecs": {
            "hwcpu_policy": "string_type_parameter",
            "hwnuma_nodes": "string_type_parameter",
        },
        "FloatingIpsCreateReq": {"pool": "public1"},
        # "ImageMetadataPostReq": {
        #     "metadata": {"custom_type_parameter": "ImagemetadatapostreqMetadata"}
        # },
        # "ImageMetadataPutReq": {
        #     "metadata": {"custom_type_parameter": "ImagemetadataputreqMetadata"}
        # },
        "ImagemetadatapostreqMetadata": {
            "kernel_id": "string_type_parameter",
            "label": "string_type_parameter",
        },
        "ImagemetadataputreqMetadata": {
            "auto_disk_config": "string_type_parameter",
            "label": "string_type_parameter",
        },
        # "KeypairsImportPostReq": {
        #     "keypair": {"custom_type_parameter": "KeypairsimportpostreqKeypair"}
        # },
        "KeypairsimportpostreqKeypair": {
            "name": "test-keypair-1",
            "type": None,
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova",
            "user_id": None,
        },
        # "SecurityGroupDefaultRulesCreateReq": {
        #     "security_group_default_rule": {
        #         "custom_type_parameter": "SecuritygroupdefaultrulescreatereqSecurityGroupDefaultRule"
        #     }
        # },
        # "SecurityGroupRulesPostReq": {
        #     "security_group_rule": {
        #         "custom_type_parameter": "SecuritygrouprulespostreqSecurityGroupRule"
        #     }
        # },
        "SecuritygroupdefaultrulescreatereqSecurityGroupDefaultRule": {
            "cidr": "string_type_parameter",
            "from_port": "string_type_parameter",
            "ip_protocol": "string_type_parameter",
            "to_port": "string_type_parameter",
        },
        "SecuritygrouprulespostreqSecurityGroupRule": {
            "cidr": "10.0.0.0/16",
            "from_port": 1,
            "ip_protocol": "TCP",
            "parent_group_id": "string_type_parameter",
            "to_port": 1,
        },
        # "ServerGroupsPostReq": {
        #     "server_group": {"custom_type_parameter": "ServergroupspostreqServerGroup"}
        # },
        # "ServerMetadataAllReq": {
        #     "metadata": {"custom_type_parameter": "ServermetadataallreqMetadata"}
        # },
        # "ServerTagsPutAllReq": {"tags": {"custom_type_parameter": "list[Tag]"}},
        "ServergroupspostreqServerGroup": {
            "name": "string_type_parameter",
            "policy": "string_type_parameter",
            # "rules": {"custom_type_parameter": "ServergroupspostreqServerGroupRules"},
        },
        "ServergroupspostreqServerGroupRules": {"max_server_per_host": 1},
        "ServermetadataallreqMetadata": {"foo": "string_type_parameter"},
        # "SnapshotCreateAssistedReq": {
        #     "snapshot": {"custom_type_parameter": "SnapshotcreateassistedreqSnapshot"}
        # },
        "SnapshotcreateassistedreqSnapshot": {
            # "create_info": {
            #     "custom_type_parameter": "SnapshotcreateassistedreqSnapshotCreateInfo"
            # },
            "volume_id": "string_type_parameter",
        },
        "SnapshotcreateassistedreqSnapshotCreateInfo": {
            "id": "string_type_parameter",
            "new_file": "string_type_parameter",
            "snapshot_id": "string_type_parameter",
            "type": "string_type_parameter",
        },
        "Tag": {},
    }
}
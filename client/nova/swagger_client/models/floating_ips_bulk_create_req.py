# coding: utf-8

"""
    Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FloatingIpsBulkCreateReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'floating_ips_bulk_create': 'FloatingipsbulkcreatereqFloatingIpsBulkCreate'
    }

    attribute_map = {
        'floating_ips_bulk_create': 'floating_ips_bulk_create'
    }

    def __init__(self, floating_ips_bulk_create=None, _configuration=None):  # noqa: E501
        """FloatingIpsBulkCreateReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._floating_ips_bulk_create = None
        self.discriminator = None

        if floating_ips_bulk_create is not None:
            self.floating_ips_bulk_create = floating_ips_bulk_create

    @property
    def floating_ips_bulk_create(self):
        """Gets the floating_ips_bulk_create of this FloatingIpsBulkCreateReq.  # noqa: E501


        :return: The floating_ips_bulk_create of this FloatingIpsBulkCreateReq.  # noqa: E501
        :rtype: FloatingipsbulkcreatereqFloatingIpsBulkCreate
        """
        return self._floating_ips_bulk_create

    @floating_ips_bulk_create.setter
    def floating_ips_bulk_create(self, floating_ips_bulk_create):
        """Sets the floating_ips_bulk_create of this FloatingIpsBulkCreateReq.


        :param floating_ips_bulk_create: The floating_ips_bulk_create of this FloatingIpsBulkCreateReq.  # noqa: E501
        :type: FloatingipsbulkcreatereqFloatingIpsBulkCreate
        """

        self._floating_ips_bulk_create = floating_ips_bulk_create

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FloatingIpsBulkCreateReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FloatingIpsBulkCreateReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FloatingIpsBulkCreateReq):
            return True

        return self.to_dict() != other.to_dict()

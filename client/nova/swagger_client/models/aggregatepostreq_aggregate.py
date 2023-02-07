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


class AggregatepostreqAggregate(object):
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
        'name': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, name=None, availability_zone=None, _configuration=None):  # noqa: E501
        """AggregatepostreqAggregate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._availability_zone = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def name(self):
        """Gets the name of this AggregatepostreqAggregate.  # noqa: E501


        :return: The name of this AggregatepostreqAggregate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AggregatepostreqAggregate.


        :param name: The name of this AggregatepostreqAggregate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AggregatepostreqAggregate.  # noqa: E501


        :return: The availability_zone of this AggregatepostreqAggregate.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AggregatepostreqAggregate.


        :param availability_zone: The availability_zone of this AggregatepostreqAggregate.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

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
        if issubclass(AggregatepostreqAggregate, dict):
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
        if not isinstance(other, AggregatepostreqAggregate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatepostreqAggregate):
            return True

        return self.to_dict() != other.to_dict()

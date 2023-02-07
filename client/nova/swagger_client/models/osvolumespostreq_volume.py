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


class OsvolumespostreqVolume(object):
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
        'availability_zone': 'str',
        'display_name': 'str',
        'display_description': 'str',
        'size': 'int'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'display_name': 'display_name',
        'display_description': 'display_description',
        'size': 'size'
    }

    def __init__(self, availability_zone=None, display_name=None, display_description=None, size=None, _configuration=None):  # noqa: E501
        """OsvolumespostreqVolume - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._availability_zone = None
        self._display_name = None
        self._display_description = None
        self._size = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if display_name is not None:
            self.display_name = display_name
        if display_description is not None:
            self.display_description = display_description
        if size is not None:
            self.size = size

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OsvolumespostreqVolume.  # noqa: E501


        :return: The availability_zone of this OsvolumespostreqVolume.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OsvolumespostreqVolume.


        :param availability_zone: The availability_zone of this OsvolumespostreqVolume.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def display_name(self):
        """Gets the display_name of this OsvolumespostreqVolume.  # noqa: E501


        :return: The display_name of this OsvolumespostreqVolume.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OsvolumespostreqVolume.


        :param display_name: The display_name of this OsvolumespostreqVolume.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_description(self):
        """Gets the display_description of this OsvolumespostreqVolume.  # noqa: E501


        :return: The display_description of this OsvolumespostreqVolume.  # noqa: E501
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this OsvolumespostreqVolume.


        :param display_description: The display_description of this OsvolumespostreqVolume.  # noqa: E501
        :type: str
        """

        self._display_description = display_description

    @property
    def size(self):
        """Gets the size of this OsvolumespostreqVolume.  # noqa: E501


        :return: The size of this OsvolumespostreqVolume.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OsvolumespostreqVolume.


        :param size: The size of this OsvolumespostreqVolume.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(OsvolumespostreqVolume, dict):
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
        if not isinstance(other, OsvolumespostreqVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OsvolumespostreqVolume):
            return True

        return self.to_dict() != other.to_dict()
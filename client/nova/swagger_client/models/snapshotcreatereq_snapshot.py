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


class SnapshotcreatereqSnapshot(object):
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
        'display_name': 'str',
        'display_description': 'str',
        'volume_id': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'display_name': 'display_name',
        'display_description': 'display_description',
        'volume_id': 'volume_id',
        'force': 'force'
    }

    def __init__(self, display_name=None, display_description=None, volume_id=None, force=None, _configuration=None):  # noqa: E501
        """SnapshotcreatereqSnapshot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._display_description = None
        self._volume_id = None
        self._force = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if display_description is not None:
            self.display_description = display_description
        if volume_id is not None:
            self.volume_id = volume_id
        if force is not None:
            self.force = force

    @property
    def display_name(self):
        """Gets the display_name of this SnapshotcreatereqSnapshot.  # noqa: E501


        :return: The display_name of this SnapshotcreatereqSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SnapshotcreatereqSnapshot.


        :param display_name: The display_name of this SnapshotcreatereqSnapshot.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_description(self):
        """Gets the display_description of this SnapshotcreatereqSnapshot.  # noqa: E501


        :return: The display_description of this SnapshotcreatereqSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this SnapshotcreatereqSnapshot.


        :param display_description: The display_description of this SnapshotcreatereqSnapshot.  # noqa: E501
        :type: str
        """

        self._display_description = display_description

    @property
    def volume_id(self):
        """Gets the volume_id of this SnapshotcreatereqSnapshot.  # noqa: E501


        :return: The volume_id of this SnapshotcreatereqSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SnapshotcreatereqSnapshot.


        :param volume_id: The volume_id of this SnapshotcreatereqSnapshot.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def force(self):
        """Gets the force of this SnapshotcreatereqSnapshot.  # noqa: E501


        :return: The force of this SnapshotcreatereqSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this SnapshotcreatereqSnapshot.


        :param force: The force of this SnapshotcreatereqSnapshot.  # noqa: E501
        :type: bool
        """

        self._force = force

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
        if issubclass(SnapshotcreatereqSnapshot, dict):
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
        if not isinstance(other, SnapshotcreatereqSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotcreatereqSnapshot):
            return True

        return self.to_dict() != other.to_dict()

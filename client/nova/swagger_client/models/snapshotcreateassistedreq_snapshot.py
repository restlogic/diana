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


class SnapshotcreateassistedreqSnapshot(object):
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
        'volume_id': 'str',
        'create_info': 'SnapshotcreateassistedreqSnapshotCreateInfo'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'create_info': 'create_info'
    }

    def __init__(self, volume_id=None, create_info=None, _configuration=None):  # noqa: E501
        """SnapshotcreateassistedreqSnapshot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._volume_id = None
        self._create_info = None
        self.discriminator = None

        if volume_id is not None:
            self.volume_id = volume_id
        if create_info is not None:
            self.create_info = create_info

    @property
    def volume_id(self):
        """Gets the volume_id of this SnapshotcreateassistedreqSnapshot.  # noqa: E501


        :return: The volume_id of this SnapshotcreateassistedreqSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SnapshotcreateassistedreqSnapshot.


        :param volume_id: The volume_id of this SnapshotcreateassistedreqSnapshot.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def create_info(self):
        """Gets the create_info of this SnapshotcreateassistedreqSnapshot.  # noqa: E501


        :return: The create_info of this SnapshotcreateassistedreqSnapshot.  # noqa: E501
        :rtype: SnapshotcreateassistedreqSnapshotCreateInfo
        """
        return self._create_info

    @create_info.setter
    def create_info(self, create_info):
        """Sets the create_info of this SnapshotcreateassistedreqSnapshot.


        :param create_info: The create_info of this SnapshotcreateassistedreqSnapshot.  # noqa: E501
        :type: SnapshotcreateassistedreqSnapshotCreateInfo
        """

        self._create_info = create_info

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
        if issubclass(SnapshotcreateassistedreqSnapshot, dict):
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
        if not isinstance(other, SnapshotcreateassistedreqSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotcreateassistedreqSnapshot):
            return True

        return self.to_dict() != other.to_dict()
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


class CloudpipeupdatereqConfigureProject(object):
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
        'vpn_ip': 'str',
        'vpn_port': 'str'
    }

    attribute_map = {
        'vpn_ip': 'vpn_ip',
        'vpn_port': 'vpn_port'
    }

    def __init__(self, vpn_ip=None, vpn_port=None, _configuration=None):  # noqa: E501
        """CloudpipeupdatereqConfigureProject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vpn_ip = None
        self._vpn_port = None
        self.discriminator = None

        if vpn_ip is not None:
            self.vpn_ip = vpn_ip
        if vpn_port is not None:
            self.vpn_port = vpn_port

    @property
    def vpn_ip(self):
        """Gets the vpn_ip of this CloudpipeupdatereqConfigureProject.  # noqa: E501


        :return: The vpn_ip of this CloudpipeupdatereqConfigureProject.  # noqa: E501
        :rtype: str
        """
        return self._vpn_ip

    @vpn_ip.setter
    def vpn_ip(self, vpn_ip):
        """Sets the vpn_ip of this CloudpipeupdatereqConfigureProject.


        :param vpn_ip: The vpn_ip of this CloudpipeupdatereqConfigureProject.  # noqa: E501
        :type: str
        """

        self._vpn_ip = vpn_ip

    @property
    def vpn_port(self):
        """Gets the vpn_port of this CloudpipeupdatereqConfigureProject.  # noqa: E501


        :return: The vpn_port of this CloudpipeupdatereqConfigureProject.  # noqa: E501
        :rtype: str
        """
        return self._vpn_port

    @vpn_port.setter
    def vpn_port(self, vpn_port):
        """Sets the vpn_port of this CloudpipeupdatereqConfigureProject.


        :param vpn_port: The vpn_port of this CloudpipeupdatereqConfigureProject.  # noqa: E501
        :type: str
        """

        self._vpn_port = vpn_port

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
        if issubclass(CloudpipeupdatereqConfigureProject, dict):
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
        if not isinstance(other, CloudpipeupdatereqConfigureProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudpipeupdatereqConfigureProject):
            return True

        return self.to_dict() != other.to_dict()
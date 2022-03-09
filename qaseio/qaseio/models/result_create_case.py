# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResultCreateCase(object):
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
        'title': 'str',
        'suite_title': 'str',
        'description': 'str',
        'layer': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'title': 'title',
        'suite_title': 'suite_title',
        'description': 'description',
        'layer': 'layer',
        'severity': 'severity'
    }

    def __init__(self, title=None, suite_title=None, description=None, layer=None, severity=None):  # noqa: E501
        """ResultCreateCase - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._suite_title = None
        self._description = None
        self._layer = None
        self._severity = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if suite_title is not None:
            self.suite_title = suite_title
        if description is not None:
            self.description = description
        if layer is not None:
            self.layer = layer
        if severity is not None:
            self.severity = severity

    @property
    def title(self):
        """Gets the title of this ResultCreateCase.  # noqa: E501


        :return: The title of this ResultCreateCase.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResultCreateCase.


        :param title: The title of this ResultCreateCase.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def suite_title(self):
        """Gets the suite_title of this ResultCreateCase.  # noqa: E501

        Nested suites should be separated with `TAB` symbol.  # noqa: E501

        :return: The suite_title of this ResultCreateCase.  # noqa: E501
        :rtype: str
        """
        return self._suite_title

    @suite_title.setter
    def suite_title(self, suite_title):
        """Sets the suite_title of this ResultCreateCase.

        Nested suites should be separated with `TAB` symbol.  # noqa: E501

        :param suite_title: The suite_title of this ResultCreateCase.  # noqa: E501
        :type: str
        """

        self._suite_title = suite_title

    @property
    def description(self):
        """Gets the description of this ResultCreateCase.  # noqa: E501


        :return: The description of this ResultCreateCase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResultCreateCase.


        :param description: The description of this ResultCreateCase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def layer(self):
        """Gets the layer of this ResultCreateCase.  # noqa: E501


        :return: The layer of this ResultCreateCase.  # noqa: E501
        :rtype: str
        """
        return self._layer

    @layer.setter
    def layer(self, layer):
        """Sets the layer of this ResultCreateCase.


        :param layer: The layer of this ResultCreateCase.  # noqa: E501
        :type: str
        """

        self._layer = layer

    @property
    def severity(self):
        """Gets the severity of this ResultCreateCase.  # noqa: E501


        :return: The severity of this ResultCreateCase.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ResultCreateCase.


        :param severity: The severity of this ResultCreateCase.  # noqa: E501
        :type: str
        """

        self._severity = severity

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
        if issubclass(ResultCreateCase, dict):
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
        if not isinstance(other, ResultCreateCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
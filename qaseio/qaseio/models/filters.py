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

class Filters(object):
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
        'search': 'str',
        'milestone_id': 'int',
        'suite_id': 'int',
        'severity': 'str',
        'priority': 'str',
        'type': 'str',
        'behavior': 'str',
        'automation': 'str',
        'status': 'str'
    }

    attribute_map = {
        'search': 'search',
        'milestone_id': 'milestone_id',
        'suite_id': 'suite_id',
        'severity': 'severity',
        'priority': 'priority',
        'type': 'type',
        'behavior': 'behavior',
        'automation': 'automation',
        'status': 'status'
    }

    def __init__(self, search=None, milestone_id=None, suite_id=None, severity=None, priority=None, type=None, behavior=None, automation=None, status=None):  # noqa: E501
        """Filters - a model defined in Swagger"""  # noqa: E501
        self._search = None
        self._milestone_id = None
        self._suite_id = None
        self._severity = None
        self._priority = None
        self._type = None
        self._behavior = None
        self._automation = None
        self._status = None
        self.discriminator = None
        if search is not None:
            self.search = search
        if milestone_id is not None:
            self.milestone_id = milestone_id
        if suite_id is not None:
            self.suite_id = suite_id
        if severity is not None:
            self.severity = severity
        if priority is not None:
            self.priority = priority
        if type is not None:
            self.type = type
        if behavior is not None:
            self.behavior = behavior
        if automation is not None:
            self.automation = automation
        if status is not None:
            self.status = status

    @property
    def search(self):
        """Gets the search of this Filters.  # noqa: E501

        Provide a string that will be used to search by name.  # noqa: E501

        :return: The search of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this Filters.

        Provide a string that will be used to search by name.  # noqa: E501

        :param search: The search of this Filters.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def milestone_id(self):
        """Gets the milestone_id of this Filters.  # noqa: E501

        ID of milestone.  # noqa: E501

        :return: The milestone_id of this Filters.  # noqa: E501
        :rtype: int
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id):
        """Sets the milestone_id of this Filters.

        ID of milestone.  # noqa: E501

        :param milestone_id: The milestone_id of this Filters.  # noqa: E501
        :type: int
        """

        self._milestone_id = milestone_id

    @property
    def suite_id(self):
        """Gets the suite_id of this Filters.  # noqa: E501

        ID of test suite.  # noqa: E501

        :return: The suite_id of this Filters.  # noqa: E501
        :rtype: int
        """
        return self._suite_id

    @suite_id.setter
    def suite_id(self, suite_id):
        """Sets the suite_id of this Filters.

        ID of test suite.  # noqa: E501

        :param suite_id: The suite_id of this Filters.  # noqa: E501
        :type: int
        """

        self._suite_id = suite_id

    @property
    def severity(self):
        """Gets the severity of this Filters.  # noqa: E501

        A list of severity values separated by comma. Possible values: undefined, blocker, critical, major, normal, minor, trivial   # noqa: E501

        :return: The severity of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Filters.

        A list of severity values separated by comma. Possible values: undefined, blocker, critical, major, normal, minor, trivial   # noqa: E501

        :param severity: The severity of this Filters.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def priority(self):
        """Gets the priority of this Filters.  # noqa: E501

        A list of priority values separated by comma. Possible values: undefined, high, medium, low   # noqa: E501

        :return: The priority of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Filters.

        A list of priority values separated by comma. Possible values: undefined, high, medium, low   # noqa: E501

        :param priority: The priority of this Filters.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def type(self):
        """Gets the type of this Filters.  # noqa: E501

        A list of type values separated by comma. Possible values: other, functional smoke, regression, security, usability, performance, acceptance   # noqa: E501

        :return: The type of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Filters.

        A list of type values separated by comma. Possible values: other, functional smoke, regression, security, usability, performance, acceptance   # noqa: E501

        :param type: The type of this Filters.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def behavior(self):
        """Gets the behavior of this Filters.  # noqa: E501

        A list of behavior values separated by comma. Possible values: undefined, positive negative, destructive   # noqa: E501

        :return: The behavior of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this Filters.

        A list of behavior values separated by comma. Possible values: undefined, positive negative, destructive   # noqa: E501

        :param behavior: The behavior of this Filters.  # noqa: E501
        :type: str
        """

        self._behavior = behavior

    @property
    def automation(self):
        """Gets the automation of this Filters.  # noqa: E501

        A list of values separated by comma. Possible values: is-not-automated, automated to-be-automated   # noqa: E501

        :return: The automation of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._automation

    @automation.setter
    def automation(self, automation):
        """Sets the automation of this Filters.

        A list of values separated by comma. Possible values: is-not-automated, automated to-be-automated   # noqa: E501

        :param automation: The automation of this Filters.  # noqa: E501
        :type: str
        """

        self._automation = automation

    @property
    def status(self):
        """Gets the status of this Filters.  # noqa: E501

        A list of values separated by comma. Possible values: actual, draft deprecated   # noqa: E501

        :return: The status of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Filters.

        A list of values separated by comma. Possible values: actual, draft deprecated   # noqa: E501

        :param status: The status of this Filters.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Filters, dict):
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
        if not isinstance(other, Filters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
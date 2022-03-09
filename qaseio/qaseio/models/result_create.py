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

class ResultCreate(object):
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
        'case_id': 'int',
        'case': 'ResultCreateCase',
        'status': 'str',
        'time': 'int',
        'time_ms': 'int',
        'defect': 'bool',
        'attachments': 'list[str]',
        'stacktrace': 'str',
        'comment': 'str',
        'param': 'dict(str, str)',
        'steps': 'list[ResultCreateSteps]'
    }

    attribute_map = {
        'case_id': 'case_id',
        'case': 'case',
        'status': 'status',
        'time': 'time',
        'time_ms': 'time_ms',
        'defect': 'defect',
        'attachments': 'attachments',
        'stacktrace': 'stacktrace',
        'comment': 'comment',
        'param': 'param',
        'steps': 'steps'
    }

    def __init__(self, case_id=None, case=None, status=None, time=None, time_ms=None, defect=None, attachments=None, stacktrace=None, comment=None, param=None, steps=None):  # noqa: E501
        """ResultCreate - a model defined in Swagger"""  # noqa: E501
        self._case_id = None
        self._case = None
        self._status = None
        self._time = None
        self._time_ms = None
        self._defect = None
        self._attachments = None
        self._stacktrace = None
        self._comment = None
        self._param = None
        self._steps = None
        self.discriminator = None
        if case_id is not None:
            self.case_id = case_id
        if case is not None:
            self.case = case
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time
        if time_ms is not None:
            self.time_ms = time_ms
        if defect is not None:
            self.defect = defect
        if attachments is not None:
            self.attachments = attachments
        if stacktrace is not None:
            self.stacktrace = stacktrace
        if comment is not None:
            self.comment = comment
        if param is not None:
            self.param = param
        if steps is not None:
            self.steps = steps

    @property
    def case_id(self):
        """Gets the case_id of this ResultCreate.  # noqa: E501


        :return: The case_id of this ResultCreate.  # noqa: E501
        :rtype: int
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this ResultCreate.


        :param case_id: The case_id of this ResultCreate.  # noqa: E501
        :type: int
        """

        self._case_id = case_id

    @property
    def case(self):
        """Gets the case of this ResultCreate.  # noqa: E501


        :return: The case of this ResultCreate.  # noqa: E501
        :rtype: ResultCreateCase
        """
        return self._case

    @case.setter
    def case(self, case):
        """Sets the case of this ResultCreate.


        :param case: The case of this ResultCreate.  # noqa: E501
        :type: ResultCreateCase
        """

        self._case = case

    @property
    def status(self):
        """Gets the status of this ResultCreate.  # noqa: E501


        :return: The status of this ResultCreate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResultCreate.


        :param status: The status of this ResultCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["in_progress", "passed", "failed", "blocked", "skipped", "invalid"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def time(self):
        """Gets the time of this ResultCreate.  # noqa: E501


        :return: The time of this ResultCreate.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ResultCreate.


        :param time: The time of this ResultCreate.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def time_ms(self):
        """Gets the time_ms of this ResultCreate.  # noqa: E501


        :return: The time_ms of this ResultCreate.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this ResultCreate.


        :param time_ms: The time_ms of this ResultCreate.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

    @property
    def defect(self):
        """Gets the defect of this ResultCreate.  # noqa: E501


        :return: The defect of this ResultCreate.  # noqa: E501
        :rtype: bool
        """
        return self._defect

    @defect.setter
    def defect(self, defect):
        """Sets the defect of this ResultCreate.


        :param defect: The defect of this ResultCreate.  # noqa: E501
        :type: bool
        """

        self._defect = defect

    @property
    def attachments(self):
        """Gets the attachments of this ResultCreate.  # noqa: E501


        :return: The attachments of this ResultCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this ResultCreate.


        :param attachments: The attachments of this ResultCreate.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def stacktrace(self):
        """Gets the stacktrace of this ResultCreate.  # noqa: E501


        :return: The stacktrace of this ResultCreate.  # noqa: E501
        :rtype: str
        """
        return self._stacktrace

    @stacktrace.setter
    def stacktrace(self, stacktrace):
        """Sets the stacktrace of this ResultCreate.


        :param stacktrace: The stacktrace of this ResultCreate.  # noqa: E501
        :type: str
        """

        self._stacktrace = stacktrace

    @property
    def comment(self):
        """Gets the comment of this ResultCreate.  # noqa: E501


        :return: The comment of this ResultCreate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ResultCreate.


        :param comment: The comment of this ResultCreate.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def param(self):
        """Gets the param of this ResultCreate.  # noqa: E501

        A map of parameters (name => value)  # noqa: E501

        :return: The param of this ResultCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this ResultCreate.

        A map of parameters (name => value)  # noqa: E501

        :param param: The param of this ResultCreate.  # noqa: E501
        :type: dict(str, str)
        """

        self._param = param

    @property
    def steps(self):
        """Gets the steps of this ResultCreate.  # noqa: E501


        :return: The steps of this ResultCreate.  # noqa: E501
        :rtype: list[ResultCreateSteps]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this ResultCreate.


        :param steps: The steps of this ResultCreate.  # noqa: E501
        :type: list[ResultCreateSteps]
        """

        self._steps = steps

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
        if issubclass(ResultCreate, dict):
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
        if not isinstance(other, ResultCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
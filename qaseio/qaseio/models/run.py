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

class Run(object):
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
        'id': 'int',
        'title': 'str',
        'description': 'str',
        'status': 'int',
        'status_text': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'public': 'bool',
        'stats': 'RunStats',
        'time_spent': 'int',
        'environment': 'RunEnvironment',
        'milestone': 'RunMilestone',
        'custom_fields': 'list[CustomFieldValue]',
        'tags': 'list[TagValue]',
        'cases': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'status': 'status',
        'status_text': 'status_text',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'public': 'public',
        'stats': 'stats',
        'time_spent': 'time_spent',
        'environment': 'environment',
        'milestone': 'milestone',
        'custom_fields': 'custom_fields',
        'tags': 'tags',
        'cases': 'cases'
    }

    def __init__(self, id=None, title=None, description=None, status=None, status_text=None, start_time=None, end_time=None, public=None, stats=None, time_spent=None, environment=None, milestone=None, custom_fields=None, tags=None, cases=None):  # noqa: E501
        """Run - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._description = None
        self._status = None
        self._status_text = None
        self._start_time = None
        self._end_time = None
        self._public = None
        self._stats = None
        self._time_spent = None
        self._environment = None
        self._milestone = None
        self._custom_fields = None
        self._tags = None
        self._cases = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if status_text is not None:
            self.status_text = status_text
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if public is not None:
            self.public = public
        if stats is not None:
            self.stats = stats
        if time_spent is not None:
            self.time_spent = time_spent
        if environment is not None:
            self.environment = environment
        if milestone is not None:
            self.milestone = milestone
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if tags is not None:
            self.tags = tags
        if cases is not None:
            self.cases = cases

    @property
    def id(self):
        """Gets the id of this Run.  # noqa: E501


        :return: The id of this Run.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Run.


        :param id: The id of this Run.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Run.  # noqa: E501


        :return: The title of this Run.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Run.


        :param title: The title of this Run.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Run.  # noqa: E501


        :return: The description of this Run.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Run.


        :param description: The description of this Run.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Run.  # noqa: E501


        :return: The status of this Run.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Run.


        :param status: The status of this Run.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def status_text(self):
        """Gets the status_text of this Run.  # noqa: E501


        :return: The status_text of this Run.  # noqa: E501
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """Sets the status_text of this Run.


        :param status_text: The status_text of this Run.  # noqa: E501
        :type: str
        """

        self._status_text = status_text

    @property
    def start_time(self):
        """Gets the start_time of this Run.  # noqa: E501


        :return: The start_time of this Run.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Run.


        :param start_time: The start_time of this Run.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Run.  # noqa: E501


        :return: The end_time of this Run.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Run.


        :param end_time: The end_time of this Run.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def public(self):
        """Gets the public of this Run.  # noqa: E501


        :return: The public of this Run.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Run.


        :param public: The public of this Run.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def stats(self):
        """Gets the stats of this Run.  # noqa: E501


        :return: The stats of this Run.  # noqa: E501
        :rtype: RunStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Run.


        :param stats: The stats of this Run.  # noqa: E501
        :type: RunStats
        """

        self._stats = stats

    @property
    def time_spent(self):
        """Gets the time_spent of this Run.  # noqa: E501

        Time in ms.  # noqa: E501

        :return: The time_spent of this Run.  # noqa: E501
        :rtype: int
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_spent):
        """Sets the time_spent of this Run.

        Time in ms.  # noqa: E501

        :param time_spent: The time_spent of this Run.  # noqa: E501
        :type: int
        """

        self._time_spent = time_spent

    @property
    def environment(self):
        """Gets the environment of this Run.  # noqa: E501


        :return: The environment of this Run.  # noqa: E501
        :rtype: RunEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Run.


        :param environment: The environment of this Run.  # noqa: E501
        :type: RunEnvironment
        """

        self._environment = environment

    @property
    def milestone(self):
        """Gets the milestone of this Run.  # noqa: E501


        :return: The milestone of this Run.  # noqa: E501
        :rtype: RunMilestone
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this Run.


        :param milestone: The milestone of this Run.  # noqa: E501
        :type: RunMilestone
        """

        self._milestone = milestone

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Run.  # noqa: E501


        :return: The custom_fields of this Run.  # noqa: E501
        :rtype: list[CustomFieldValue]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Run.


        :param custom_fields: The custom_fields of this Run.  # noqa: E501
        :type: list[CustomFieldValue]
        """

        self._custom_fields = custom_fields

    @property
    def tags(self):
        """Gets the tags of this Run.  # noqa: E501


        :return: The tags of this Run.  # noqa: E501
        :rtype: list[TagValue]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Run.


        :param tags: The tags of this Run.  # noqa: E501
        :type: list[TagValue]
        """

        self._tags = tags

    @property
    def cases(self):
        """Gets the cases of this Run.  # noqa: E501


        :return: The cases of this Run.  # noqa: E501
        :rtype: list[int]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """Sets the cases of this Run.


        :param cases: The cases of this Run.  # noqa: E501
        :type: list[int]
        """

        self._cases = cases

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
        if issubclass(Run, dict):
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
        if not isinstance(other, Run):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
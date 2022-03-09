# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import qaseio
from qaseio.api.milestones_api import MilestonesApi  # noqa: E501
from qaseio.rest import ApiException


class TestMilestonesApi(unittest.TestCase):
    """MilestonesApi unit test stubs"""

    def setUp(self):
        self.api = MilestonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_milestone(self):
        """Test case for create_milestone

        Create a new milestone.  # noqa: E501
        """
        pass

    def test_delete_milestone(self):
        """Test case for delete_milestone

        Delete milestone.  # noqa: E501
        """
        pass

    def test_get_milestone(self):
        """Test case for get_milestone

        Get a specific milestone.  # noqa: E501
        """
        pass

    def test_get_milestones(self):
        """Test case for get_milestones

        Get all milestones.  # noqa: E501
        """
        pass

    def test_update_milestone(self):
        """Test case for update_milestone

        Update milestone.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from qaseio.api.attachments_api import AttachmentsApi  # noqa: E501
from qaseio.rest import ApiException


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_attachment(self):
        """Test case for delete_attachment

        Remove attachment by Hash.  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get attachment by Hash.  # noqa: E501
        """
        pass

    def test_get_attachments(self):
        """Test case for get_attachments

        Get all attachments.  # noqa: E501
        """
        pass

    def test_upload_attachment(self):
        """Test case for upload_attachment

        Upload attachment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.qql_defect import QqlDefect
from qaseio.model.qql_plan import QqlPlan
from qaseio.model.qql_test_case import QqlTestCase
from qaseio.model.requirement import Requirement
from qaseio.model.result import Result
from qaseio.model.run import Run
globals()['QqlDefect'] = QqlDefect
globals()['QqlPlan'] = QqlPlan
globals()['QqlTestCase'] = QqlTestCase
globals()['Requirement'] = Requirement
globals()['Result'] = Result
globals()['Run'] = Run
from qaseio.model.search_response_all_of_result import SearchResponseAllOfResult


class TestSearchResponseAllOfResult(unittest.TestCase):
    """SearchResponseAllOfResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResponseAllOfResult(self):
        """Test SearchResponseAllOfResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResponseAllOfResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

"""
    Ory Oathkeeper API

    Documentation for all of Ory Oathkeeper's APIs.   # noqa: E501

    The version of the OpenAPI document: v1.11.7
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_hydra_client
from ory_hydra_client.api.metadata_api import MetadataApi  # noqa: E501


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_version(self):
        """Test case for get_version

        Return Running Software Version.  # noqa: E501
        """
        pass

    def test_is_alive(self):
        """Test case for is_alive

        Check HTTP Server Status  # noqa: E501
        """
        pass

    def test_is_ready(self):
        """Test case for is_ready

        Check HTTP Server and Database Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

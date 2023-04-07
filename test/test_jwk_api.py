"""
    Ory Hydra API

    Documentation for all of Ory Hydra's APIs.   # noqa: E501

    The version of the OpenAPI document: v2.1.0
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_hydra_client
from ory_hydra_client.api.jwk_api import JwkApi  # noqa: E501


class TestJwkApi(unittest.TestCase):
    """JwkApi unit test stubs"""

    def setUp(self):
        self.api = JwkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_json_web_key_set(self):
        """Test case for create_json_web_key_set

        Create JSON Web Key  # noqa: E501
        """
        pass

    def test_delete_json_web_key(self):
        """Test case for delete_json_web_key

        Delete JSON Web Key  # noqa: E501
        """
        pass

    def test_delete_json_web_key_set(self):
        """Test case for delete_json_web_key_set

        Delete JSON Web Key Set  # noqa: E501
        """
        pass

    def test_get_json_web_key(self):
        """Test case for get_json_web_key

        Get JSON Web Key  # noqa: E501
        """
        pass

    def test_get_json_web_key_set(self):
        """Test case for get_json_web_key_set

        Retrieve a JSON Web Key Set  # noqa: E501
        """
        pass

    def test_set_json_web_key(self):
        """Test case for set_json_web_key

        Set JSON Web Key  # noqa: E501
        """
        pass

    def test_set_json_web_key_set(self):
        """Test case for set_json_web_key_set

        Update a JSON Web Key Set  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

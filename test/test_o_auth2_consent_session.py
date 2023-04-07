"""
    Ory Hydra API

    Documentation for all of Ory Hydra's APIs.   # noqa: E501

    The version of the OpenAPI document: v2.1.0
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_hydra_client
from ory_hydra_client.model.accept_o_auth2_consent_request_session import AcceptOAuth2ConsentRequestSession
from ory_hydra_client.model.o_auth2_consent_request import OAuth2ConsentRequest
from ory_hydra_client.model.o_auth2_consent_session_expires_at import OAuth2ConsentSessionExpiresAt
from ory_hydra_client.model.string_slice_json_format import StringSliceJSONFormat
globals()['AcceptOAuth2ConsentRequestSession'] = AcceptOAuth2ConsentRequestSession
globals()['OAuth2ConsentRequest'] = OAuth2ConsentRequest
globals()['OAuth2ConsentSessionExpiresAt'] = OAuth2ConsentSessionExpiresAt
globals()['StringSliceJSONFormat'] = StringSliceJSONFormat
from ory_hydra_client.model.o_auth2_consent_session import OAuth2ConsentSession


class TestOAuth2ConsentSession(unittest.TestCase):
    """OAuth2ConsentSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOAuth2ConsentSession(self):
        """Test OAuth2ConsentSession"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OAuth2ConsentSession()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

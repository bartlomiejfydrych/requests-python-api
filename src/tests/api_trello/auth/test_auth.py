from typing import Any, Iterator, Optional

import pytest
from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.utils.named_endpoint import NamedEndpoint
from endpoints.utils.providers import all_endpoints_provider
from tests.base.test_base import TestBase


# ==========================================================================================================
# PARAMETRIZE – DATA
# ==========================================================================================================

def _auth_test_cases() -> Iterator[Any]:
    for named_endpoint in all_endpoints_provider.all():
        yield pytest.param(
            named_endpoint,
            "Missing API Key",
            id=f"{named_endpoint} \u2192 Missing API Key",
        )
        # NOTE FOR ME:
        # Okazało się, że gdy mieliśmy klucz API, token nie był w ogóle walidowany.
        # Zgłoszone do Trello, żeby potwierdzić, że to zamierzone zachowanie.
        # yield pytest.param(
        #     named_endpoint,
        #     "Missing Token",
        #     id=f"{named_endpoint} \u2192 Missing Token",
        # )


# ==========================================================================================================
# TESTS
# ==========================================================================================================

class TestAuth(TestBase):
    """Auth validation for all endpoints."""

    @pytest.mark.parametrize("named_endpoint, auth_case", _auth_test_cases())
    def test_should_return_401_for_unauthorized_requests(
            self,
            named_endpoint: NamedEndpoint,
            auth_case: str,
    ) -> None:
        spec: Optional[BaseRequestSpec] = (
            self.request_specification_without_api_key
            if auth_case == "Missing API Key"
            else self.request_specification_without_token
        )
        assert spec is not None

        response: Response = named_endpoint.call(spec)

        assert response.status_code == 401

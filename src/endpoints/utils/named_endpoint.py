from dataclasses import dataclass

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.utils.endpoint_call import EndpointCall


# ==========================================================================================================
# NAMED ENDPOINT
# ==========================================================================================================

@dataclass
class NamedEndpoint:
    """
    NOTE FOR ME:
    Odpowiednik NamedEndpoint z Javy.
    Owija wywołanie endpointu (EndpointCall) razem z jego nazwą, dzięki czemu w parametryzowanych
    testach (np. AuthTest) oraz w raportach widać czytelną etykietę zamiast samej lambdy.
    """

    name: str
    endpoint: EndpointCall

    def call(self, spec: BaseRequestSpec) -> Response:
        return self.endpoint(spec)

    def __str__(self) -> str:
        return self.name

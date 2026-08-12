from typing import Callable

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec

# ==========================================================================================================
# TYPE ALIASES
# ==========================================================================================================

# NOTE FOR ME:
# Java – @FunctionalInterface EndpointCall { Response call(RequestSpecification spec); }
# Python nie potrzebuje osobnego interfejsu funkcyjnego – zwykła funkcja/lambda o sygnaturze
# (BaseRequestSpec) -> Response już spełnia ten kontrakt. Ten alias typu służy wyłącznie
# czytelności i podpowiedziom typów w NamedEndpoint oraz providerach.
EndpointCall = Callable[[BaseRequestSpec], Response]

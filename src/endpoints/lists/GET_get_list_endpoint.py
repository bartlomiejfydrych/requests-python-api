from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.lists.lists_base_endpoint import list_by_id


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_list(list_id: str, spec: BaseRequestSpec) -> Response:
    return spec.get(list_by_id(list_id))


def get_get_list(list_id: str) -> Response:
    return get_list(list_id, get_specification())

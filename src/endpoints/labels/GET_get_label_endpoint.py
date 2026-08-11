from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.labels.labels_base_endpoint import label_by_id


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_label(label_id: str, spec: BaseRequestSpec) -> Response:
    return spec.get(label_by_id(label_id))


def get_get_label(label_id: str) -> Response:
    return get_label(label_id, get_specification())

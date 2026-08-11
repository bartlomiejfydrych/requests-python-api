from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.labels.labels_base_endpoint import label_by_id


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def delete_label(label_id: str, spec: BaseRequestSpec) -> Response:
    return spec.delete(label_by_id(label_id))


def delete_delete_label(label_id: str) -> Response:
    return delete_label(label_id, get_specification())

from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.labels.labels_base_endpoint import (
    ENDPOINT_LABELS,
    label_by_id,
)

from payloads.labels.PUT_update_label_payload import PutUpdateLabelPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def update_label(
        label_id: str,
        payload: Optional[PutUpdateLabelPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.put(
        label_by_id(label_id),
        params=query_params,
    )


def put_update_label(
        label_id: str,
        payload: Optional[PutUpdateLabelPayload],
) -> Response:
    return update_label(
        label_id,
        payload,
        get_specification(),
    )


# -------------------
# WITHOUT ID & PARAMS
# -------------------

def put_update_label_without_id_and_params() -> Response:
    return get_specification().put(ENDPOINT_LABELS)

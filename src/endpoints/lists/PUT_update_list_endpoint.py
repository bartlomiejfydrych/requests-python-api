from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.lists.lists_base_endpoint import (
    ENDPOINT_LISTS,
    list_by_id,
)

from payloads.lists.PUT_update_list_payload import PutUpdateListPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def update_list(
        list_id: str,
        payload: Optional[PutUpdateListPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.put(
        list_by_id(list_id),
        params=query_params,
    )


def put_update_list(
        list_id: str,
        payload: Optional[PutUpdateListPayload],
) -> Response:
    return update_list(
        list_id,
        payload,
        get_specification(),
    )


# -------------------
# WITHOUT ID & PARAMS
# -------------------

def put_update_list_without_id_and_params() -> Response:
    return get_specification().put(ENDPOINT_LISTS)

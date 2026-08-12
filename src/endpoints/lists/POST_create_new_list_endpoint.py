from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.lists.lists_base_endpoint import ENDPOINT_LISTS

from enums.query_parameters.lists.lists.list_base_query_parameters import ListBaseQueryParameters

from payloads.lists.POST_create_new_list_payload import PostCreateNewListPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def create_new_list(
        board_id: str,
        list_name: str,
        payload: Optional[PostCreateNewListPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {
        ListBaseQueryParameters.ID_BOARD.value: board_id,
        ListBaseQueryParameters.NAME.value: list_name,
    }

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.post(
        ENDPOINT_LISTS,
        params=query_params,
    )


def post_create_new_list(
        board_id: str,
        list_name: str,
        payload: Optional[PostCreateNewListPayload],
) -> Response:
    return create_new_list(
        board_id,
        list_name,
        payload,
        get_specification(),
    )


# ---------------
# WITH ANY PARAMS
# ---------------

def post_create_new_list_with_any_params(
        payload: Optional[PostCreateNewListPayload],
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return get_specification().post(
        ENDPOINT_LISTS,
        params=query_params,
    )


# --------------------
# WITHOUT QUERY PARAMS
# --------------------

def post_create_new_list_missing_required_parameters() -> Response:
    return get_specification().post(ENDPOINT_LISTS)

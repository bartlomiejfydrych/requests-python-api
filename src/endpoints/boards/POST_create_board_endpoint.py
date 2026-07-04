from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.boards.boards_base_endpoint import ENDPOINT_BOARDS

from payloads.boards.post_create_board_payload import PostCreateBoardPayload

from enums.query_parameters.boards.boards.board_base_query_parameters import BoardBaseQueryParameters


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def create_board(
        board_name: str,
        payload: Optional[PostCreateBoardPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {BoardBaseQueryParameters.NAME.value: board_name}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.post(ENDPOINT_BOARDS, params=query_params)


def post_create_board(board_name: str, payload: Optional[PostCreateBoardPayload]) -> Response:
    return create_board(board_name, payload, get_specification())


# --------------------
# WITHOUT QUERY PARAMS
# --------------------

def post_create_board_missing_required_parameters() -> Response:
    return get_specification().post(ENDPOINT_BOARDS)

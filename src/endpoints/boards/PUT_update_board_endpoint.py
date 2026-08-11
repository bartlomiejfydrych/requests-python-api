from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.boards.boards_base_endpoint import board_by_id

from payloads.boards.PUT_update_board_payload import PutUpdateBoardPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def update_board(
        board_id: str,
        payload: Optional[PutUpdateBoardPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.put(
        board_by_id(board_id),
        params=query_params,
    )


def put_update_board(
        board_id: str,
        payload: Optional[PutUpdateBoardPayload],
) -> Response:
    return update_board(board_id, payload, get_specification())

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.boards.boards_base_endpoint import board_by_id


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def delete_board(board_id: str, spec: BaseRequestSpec) -> Response:
    return spec.delete(board_by_id(board_id))


def delete_delete_board(board_id: str) -> Response:
    return delete_board(board_id, get_specification())

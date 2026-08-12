from typing import Iterator

from endpoints.boards.DEL_delete_board_endpoint import delete_board
from endpoints.boards.GET_get_board_endpoint import get_board
from endpoints.boards.POST_create_board_endpoint import create_board
from endpoints.boards.PUT_update_board_endpoint import update_board
from endpoints.boards.boards_base_endpoint import ENDPOINT_BOARDS
from endpoints.utils.named_endpoint import NamedEndpoint

# ==========================================================================================================
# CONSTANTS
# ==========================================================================================================

_DUMMY_ID = "dummyId"
_ENDPOINT = ENDPOINT_BOARDS


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def all() -> Iterator[NamedEndpoint]:
    yield NamedEndpoint(f"DELETE {_ENDPOINT}/{{id}}", lambda spec: delete_board(_DUMMY_ID, spec))
    yield NamedEndpoint(f"GET {_ENDPOINT}/{{id}}", lambda spec: get_board(_DUMMY_ID, spec))
    yield NamedEndpoint(f"POST {_ENDPOINT}", lambda spec: create_board("testBoard", None, spec))
    yield NamedEndpoint(f"PUT {_ENDPOINT}/{{id}}", lambda spec: update_board(_DUMMY_ID, None, spec))

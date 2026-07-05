import json

from requests import Response

from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.boards.GET_get_board_endpoint import get_get_board
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board

from tests.base.test_base import TestBase


class TestPostCreateBoard(TestBase):

    # ==========================================================================================================
    # TESTS
    # ==========================================================================================================

    def test_should_create_board(self) -> None:
        # POST
        response: Response = post_create_board("Nazwa tablicy 1", None)
        print(json.dumps(response.json(), indent=4))
        assert response.status_code == 200
        board_id: str = response.json()["id"]
        # GET
        response = get_get_board(board_id)
        print(json.dumps(response.json(), indent=4))
        assert response.status_code == 200
        # DELETE
        response = delete_delete_board(board_id)
        print(json.dumps(response.json(), indent=4))
        assert response.status_code == 200

from typing import Optional

import pytest
from requests import Response

from configuration.config import get_trello_id
from dto.boards.POST_create_board_dto import POST_CreateBoardDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from expected_responses.boards.POST_create_board_expected import P1_EXPECTED_POST_BOARD_RESPONSE
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects
from utils_tests.POST_create_board_utils import prepare_expected_response_post, validate_get_against_post


class TestPostCreateBoard(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    board_id: Optional[str] = None
    trello_id: str = get_trello_id()

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    # ----------
    # AFTER EACH
    # ----------

    @pytest.fixture(autouse=True)
    def delete_board(self):
        yield
        if self.board_id is not None:
            response_delete: Response = delete_delete_board(self.board_id)
            assert response_delete.status_code == 200
            self.board_id = None

    # ==========================================================================================================
    # DEBUG
    # ==========================================================================================================

    # To run it, add the word "test" before the '_' character at the beginning of the method name
    def _debug_delete_board(self) -> None:
        your_board_id: str = "68724f5bfffa6577a4dc0dbb"
        response_delete: Response = delete_delete_board(your_board_id)
        assert response_delete.status_code == 200

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_create_board_whose_name_contains_special_characters_and_numbers(self) -> None:
        board_name: str = (
            "!\"#$%&\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
            "ęĘóÓąĄśŚłŁżŻźŹćĆńŃ"
            f"{self.faker.random_number()}"
        )
        # POST
        response_post: Response = post_create_board(board_name, None)
        assert response_post.status_code == 200
        self.board_id = response_post.json()["id"]
        response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
        expected_response_post_dto: POST_CreateBoardDto = prepare_expected_response_post(
            P1_EXPECTED_POST_BOARD_RESPONSE, response_post_dto, board_name
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

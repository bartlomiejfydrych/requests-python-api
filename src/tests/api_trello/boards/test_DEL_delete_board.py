from requests import Response

from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.GET_get_board_endpoint import get_get_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from tests.base.test_base import TestBase
from utils.utils_compare import compare_response_with_json
from utils_tests.boards.POST_create_board_utils import generate_random_board_name


class TestDelDeleteBoard(TestBase):
    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_delete_board(self) -> None:
        expected_response: str = """
        {
            "_value": null
        }
        """

        # POST
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        board_id: str = response_post.json()["id"]
        # DELETE
        response_delete: Response = delete_delete_board(board_id)
        assert response_delete.status_code == 200
        compare_response_with_json(response_delete, expected_response)
        # GET
        response_get: Response = get_get_board(board_id)
        assert response_get.status_code == 404
        assert response_get.text == "The requested resource was not found."

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    def test_n1_should_not_delete_board_with_id_does_not_have_access_to(self) -> None:
        # ARRANGE
        board_id: str = "5f5127e8f150fe5f98bb1267"
        # ACT
        response_delete: Response = delete_delete_board(board_id)
        # ASSERT
        assert response_delete.status_code == 401
        assert response_delete.text == "unauthorized permission requested"

    def test_n2_should_not_delete_non_existent_board(self) -> None:
        # ARRANGE
        board_id: str = "68063bdc4bdbd152d658851a"
        # ACT
        response_delete: Response = delete_delete_board(board_id)
        # ASSERT
        assert response_delete.status_code == 404
        assert response_delete.text == "The requested resource was not found."

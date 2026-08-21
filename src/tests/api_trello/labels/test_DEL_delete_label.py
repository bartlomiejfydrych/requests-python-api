from typing import Optional

import pytest
from requests import Response

from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.labels.DEL_delete_label_endpoint import delete_delete_label
from endpoints.labels.GET_get_label_endpoint import get_get_label
from endpoints.labels.POST_create_label_endpoint import post_create_label
from tests.base.test_base import TestBase
from utils.utils_compare import compare_response_with_json
from utils_tests.boards.POST_create_board_utils import generate_random_board_name


class TestDelDeleteLabel(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: Optional[str] = None

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    # NOTE FOR ME: Java uses @BeforeEach/@AfterEach here (not @BeforeAll/@AfterAll like the other label
    # tests) - a fresh board is created before EVERY test and torn down after. pytest's default fixture
    # scope is already "function", so a plain (non-class-scoped) autouse fixture matches this 1:1.

    @pytest.fixture(autouse=True)
    def setup_and_teardown_board(self):
        # -----------
        # BEFORE EACH
        # -----------

        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        self.board_id = response_post.json()["id"]

        yield

        # ----------
        # AFTER EACH
        # ----------

        if self.board_id is not None:
            response_delete: Response = delete_delete_board(self.board_id)
            assert response_delete.status_code == 200
            self.board_id = None

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_delete_label(self) -> None:
        label_name: str = "TEST – Delete Label"
        label_color: Optional[str] = None
        expected_response: str = """
        {
            "limits": {

            }
        }
        """

        # POST
        response_post: Response = post_create_label(self.board_id, label_name, label_color)
        assert response_post.status_code == 200
        label_id: str = response_post.json()["id"]
        # DELETE
        response_delete: Response = delete_delete_label(label_id)
        assert response_delete.status_code == 200
        compare_response_with_json(response_delete, expected_response)
        # GET
        response_get: Response = get_get_label(label_id)
        assert response_get.status_code == 404
        assert response_get.text == "The requested resource was not found."

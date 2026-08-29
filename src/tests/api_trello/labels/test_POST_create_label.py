from collections.abc import Generator
from typing import Optional

import pytest
from requests import Response

from dto.labels.POST_create_label_dto import PostCreateLabelDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.labels.POST_create_label_endpoint import post_create_label, post_create_label_with_any_params
from enums.query_parameters_values.labels.common.color import Color
from expected_responses.labels.POST_create_label_expected import (
    PostCreateLabelExpected,
    EXPECTED_POST_LABEL_RESPONSE_INVALID_ID,
    EXPECTED_POST_LABEL_RESPONSE_INVALID_COLOR,
)
from payloads.labels.POST_create_label_payload import PostCreateLabelPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_random import pick_random_enum
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.labels.POST_create_label_utils import validate_get_against_post


class TestPostCreateLabel(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: str

    # NOTE FOR ME: Java also declares `labelName`/`labelColor` as class fields, but no test ever reads a value
    # set by a previous test - each test sets and consumes them within its own body. So unlike `board_id`
    # (which genuinely needs BEFORE ALL/AFTER ALL sharing), they're kept as plain local variables here.

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    @pytest.fixture(scope="class", autouse=True)
    def setup_create_board(self, request) -> Generator[None, None, None]:
        # ----------
        # BEFORE ALL
        # ----------

        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        request.cls.board_id = response_post.json()["id"]

        yield

        # ---------
        # AFTER ALL
        # ---------

        response_delete: Response = delete_delete_board(request.cls.board_id)
        assert response_delete.status_code == 200

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_create_label_with_correct_values_and_name_with_special_characters_and_numbers(
            self,
    ) -> None:
        label_name: str = get_all_characters_set_in_random_order()
        label_color: Color = pick_random_enum(Color)

        # POST
        response_post: Response = post_create_label(self.board_id, label_name, label_color.value)
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        expected_response_post_dto: PostCreateLabelDto = (
            PostCreateLabelExpected.base()
            .with_id(response_post_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(label_color)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p2_should_create_label_when_name_have_one_character_and_color_is_null(self) -> None:
        label_name: str = get_random_single_char_alphanumeric()
        label_color: Optional[str] = None

        # POST
        response_post: Response = post_create_label(self.board_id, label_name, label_color)
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        expected_response_post_dto: PostCreateLabelDto = (
            PostCreateLabelExpected.base()
            .with_id(response_post_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(label_color)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p4_should_create_label_when_label_name_is_empty_string(self) -> None:
        # NOTE: A label without a name is created, but it probably shouldn't be.

        label_name: str = ""
        label_color: Color = Color.PURPLE

        # POST
        response_post: Response = post_create_label(self.board_id, label_name, label_color.value)
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        expected_response_post_dto: PostCreateLabelDto = (
            PostCreateLabelExpected.base()
            .with_id(response_post_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(label_color)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p5_should_create_label_when_label_color_is_missing(self) -> None:
        # NOTE: A label without a color is created, but it probably shouldn't be

        label_name: str = get_random_single_char_alphanumeric()

        payload: PostCreateLabelPayload = PostCreateLabelPayload(
            id_board=self.board_id,
            name=label_name,
        )

        # POST
        response_post: Response = post_create_label_with_any_params(payload)
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        expected_response_post_dto: PostCreateLabelDto = (
            PostCreateLabelExpected.base()
            .with_id(response_post_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(None)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p6_should_create_label_when_label_color_is_empty_string(self) -> None:
        # NOTE: A label without a color is created, but it probably shouldn't be

        label_name: str = get_random_single_char_alphanumeric()
        label_color: str = ""

        # POST
        response_post: Response = post_create_label(self.board_id, label_name, label_color)
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        expected_response_post_dto: PostCreateLabelDto = (
            PostCreateLabelExpected.base()
            .with_id(response_post_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(None)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # -------
    # idBoard
    # -------

    def test_n1_should_not_create_label_when_board_id_is_missing(self) -> None:
        # ARRANGE
        payload: PostCreateLabelPayload = PostCreateLabelPayload(
            name="N1 Label Name",
            color=Color.YELLOW.value,
        )
        # ACT
        response_post: Response = post_create_label_with_any_params(payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_LABEL_RESPONSE_INVALID_ID)

    @pytest.mark.parametrize(
        "test_id, test_description, board_id",
        [
            pytest.param("N2", "should_not_create_label_when_board_id_is_null", None, id="N2"),
            pytest.param("N3", "should_not_create_label_when_board_id_is_empty_string", "", id="N3"),
            pytest.param("N4", "should_not_create_label_when_board_id_non_existent", "999999", id="N4"),
            pytest.param("N5", "should_not_create_label_when_board_id_is_incorrect", "Text", id="N5"),
        ],
    )
    def test_should_not_create_label_with_invalid_board_id(
            self,
            test_id: str,
            test_description: str,
            board_id: Optional[str]
    ) -> None:
        # ACT
        response_post: Response = post_create_label(board_id, f"{test_id} Label Name", Color.PURPLE.value)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_LABEL_RESPONSE_INVALID_ID)

    # ----
    # name
    # ----

    def test_n6_should_not_create_label_when_label_name_is_missing(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
          "message": "invalid value for name",
          "error": "BAD_REQUEST_ERROR"
        }
        """
        payload: PostCreateLabelPayload = PostCreateLabelPayload(
            id_board=self.board_id,
            color=Color.PURPLE.value,
        )
        # ACT
        response_post: Response = post_create_label_with_any_params(payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, expected_response)

    # -----
    # color
    # -----

    def test_n7_should_not_create_label_when_label_color_is_incorrect(self) -> None:
        # ACT
        response_post: Response = post_create_label(self.board_id, "N11 Label Name", "KEK123")
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_LABEL_RESPONSE_INVALID_COLOR)

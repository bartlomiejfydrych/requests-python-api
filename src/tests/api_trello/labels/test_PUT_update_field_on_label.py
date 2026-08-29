from collections.abc import Generator
from typing import Optional

import pytest
from requests import Response

from dto.labels.POST_create_label_dto import PostCreateLabelDto
from dto.labels.PUT_update_field_on_label_dto import PutUpdateFieldOnLabelDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.labels.POST_create_label_endpoint import post_create_label
from endpoints.labels.PUT_update_field_on_label_endpoint import (
    put_update_field_on_label,
    put_update_field_on_label_custom_field,
    put_update_field_on_label_without_field_value,
)
from enums.query_parameters.labels.label_base_query_parameters import LabelBaseQueryParameters
from enums.query_parameters_values.labels.common.color import Color
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_random import pick_random_enum
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.labels.POST_create_label_utils import generate_random_label_color, generate_random_label_name
from utils_tests.labels.PUT_update_field_on_label_utils import validate_get_against_put


class TestPutUpdateFieldOnLabel(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: Optional[str] = None
    # LABEL
    label_id: str
    # NOTE: The label object created below acts as our "expected response" - we mutate its fields in place
    # as each positive test changes something on the real label.
    expected_label_dto: PostCreateLabelDto

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    @pytest.fixture(scope="class", autouse=True)
    def setup_create_board_and_label(self, request) -> Generator[None, None, None]:
        # ----------
        # BEFORE ALL
        # ----------
        # BOARD
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        request.cls.board_id = response_post.json()["id"]
        # LABEL
        response_post = post_create_label(
            request.cls.board_id, generate_random_label_name(), generate_random_label_color()
        )
        assert response_post.status_code == 200
        response_post_dto: PostCreateLabelDto = deserialize_and_validate_json(response_post, PostCreateLabelDto)
        request.cls.expected_label_dto = response_post_dto
        request.cls.label_id = response_post_dto.id

        yield

        # ---------
        # AFTER ALL
        # ---------
        if request.cls.board_id is not None:
            response_delete: Response = delete_delete_board(request.cls.board_id)
            assert response_delete.status_code == 200
            request.cls.board_id = None
            request.cls.label_id = None

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    # ----
    # name
    # ----

    def test_p1_should_update_label_field_name_with_special_characters_and_numbers(self) -> None:
        label_field_value: str = get_all_characters_set_in_random_order()
        self.expected_label_dto.name = label_field_value

        # PUT
        response_put: Response = put_update_field_on_label(
            self.label_id, LabelBaseQueryParameters.NAME, label_field_value
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        compare_objects(response_put_dto, self.expected_label_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p2_should_update_label_field_name_with_one_character(self) -> None:
        label_field_value: str = get_random_single_char_alphanumeric()
        self.expected_label_dto.name = label_field_value

        # PUT
        response_put: Response = put_update_field_on_label(
            self.label_id, LabelBaseQueryParameters.NAME, label_field_value
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        compare_objects(response_put_dto, self.expected_label_dto)
        # GET
        validate_get_against_put(response_put_dto)

    @pytest.mark.flaky
    @pytest.mark.skip(
        reason="Flaky test – Sometimes fields become empty/null, sometimes they are not changed at all"
    )
    def test_p3_should_update_label_field_name_with_empty_string(self) -> None:
        # WARNING: Flaky test – Data shouldn't change, but sometimes it does.

        label_field_value: str = ""
        self.expected_label_dto.name = label_field_value

        # PUT
        response_put: Response = put_update_field_on_label(
            self.label_id, LabelBaseQueryParameters.NAME, label_field_value
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        compare_objects(response_put_dto, self.expected_label_dto)
        # GET
        validate_get_against_put(response_put_dto)

    # -----
    # color
    # -----

    def test_p4_should_update_label_field_color_with_one_of_correct_colors(self) -> None:
        random_color: Color = pick_random_enum(Color)
        label_field_value: str = random_color.value
        self.expected_label_dto.color = label_field_value

        # PUT
        response_put: Response = put_update_field_on_label(
            self.label_id, LabelBaseQueryParameters.COLOR, label_field_value
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        compare_objects(response_put_dto, self.expected_label_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p6_should_update_label_field_color_with_empty_string(self) -> None:
        label_field_value: str = ""
        self.expected_label_dto.color = None

        # PUT
        response_put: Response = put_update_field_on_label(
            self.label_id, LabelBaseQueryParameters.COLOR, label_field_value
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        compare_objects(response_put_dto, self.expected_label_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p7_should_update_label_field_color_without_value(self) -> None:
        # NOTE: If we don't provide a value, it changes to 'null', and it probably shouldn't be changed.

        # PUT
        response_put: Response = put_update_field_on_label_without_field_value(
            self.label_id, LabelBaseQueryParameters.COLOR
        )
        assert response_put.status_code == 200
        response_put_dto: PutUpdateFieldOnLabelDto = deserialize_and_validate_json(
            response_put, PutUpdateFieldOnLabelDto
        )
        expected_response_post_dto: PostCreateLabelDto = self.expected_label_dto
        expected_response_post_dto.color = None
        compare_objects(response_put_dto, expected_response_post_dto)
        # GET
        validate_get_against_put(response_put_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # --
    # id
    # --

    def test_n3_should_not_update_label_field_with_non_existent_id(self) -> None:
        # ARRANGE
        label_id: str = "999999999999999999999999"
        # ACT
        response_put: Response = put_update_field_on_label(
            label_id, LabelBaseQueryParameters.NAME, "Update Label Field – negative test"
        )
        # ASSERT
        assert response_put.status_code == 404
        assert response_put.text == "The requested resource was not found."

    def test_n4_should_not_update_label_field_with_incorrect_id(self) -> None:
        # ARRANGE
        label_id: str = "Kek123"
        # ACT
        response_put: Response = put_update_field_on_label(
            label_id, LabelBaseQueryParameters.NAME, "Update Label Field – negative test"
        )
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid id"

    # -----
    # field
    # -----

    def test_n5_should_not_update_label_field_with_incorrect_field_name(self) -> None:
        # ARRANGE
        incorrect_field_name: str = "uses"
        # ACT
        response_put: Response = put_update_field_on_label_custom_field(
            self.label_id, incorrect_field_name, "Update Label Field – negative test"
        )
        # ASSERT
        assert response_put.status_code == 404
        assert response_put.text.startswith(f"Cannot PUT /1/labels/{self.label_id}/")

    # ----
    # name
    # ----

    def test_n1_should_not_update_label_field_name_without_value(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
          "message": "invalid value for value",
          "error": "BAD_REQUEST_ERROR"
        }
        """
        # ACT
        response_put: Response = put_update_field_on_label_without_field_value(
            self.label_id, LabelBaseQueryParameters.NAME
        )
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, expected_response)

    # -----
    # color
    # -----

    def test_n2_should_not_update_label_field_color_with_incorrect_value(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
            "message": "invalid value for value",
            "error": "ERROR"
        }
        """
        # ACT
        response_put: Response = put_update_field_on_label(self.label_id, LabelBaseQueryParameters.COLOR, "KEK123")
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, expected_response)

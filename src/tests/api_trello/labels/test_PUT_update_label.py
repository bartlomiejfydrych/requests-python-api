from collections.abc import Generator

import pytest
from requests import Response

from dto.labels.GET_get_label_dto import GetLabelDto
from dto.labels.PUT_update_label_dto import PutUpdateLabelDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.labels.GET_get_label_endpoint import get_get_label
from endpoints.labels.POST_create_label_endpoint import post_create_label
from endpoints.labels.PUT_update_label_endpoint import put_update_label
from enums.query_parameters_values.labels.common.color import Color
from expected_responses.labels.PUT_update_label_expected import (
    PutUpdateLabelExpected,
    EXPECTED_PUT_LABEL_RESPONSE_INVALID_COLOR,
)
from payloads.labels.PUT_update_label_payload import PutUpdateLabelPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import (
    deserialize_and_validate_json,
    deserialize_and_validate_json_with_business_rules,
)
from utils.utils_compare import compare_objects, compare_response_with_json, assert_satisfies_any_of
from utils.utils_random import pick_random_enum
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.labels.POST_create_label_utils import generate_random_label_color, generate_random_label_name
from utils_tests.labels.PUT_update_label_utils import validate_get_against_put


class TestPutUpdateLabel(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: str
    # LABEL
    label_id: str

    # NOTE FOR ME: Java also declares `labelName`/`labelColor` as class fields, but (same as in
    # POST_CreateLabelTest) no test ever reads a value set by a previous test - kept as plain locals here.

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
        request.cls.label_id = response_post.json()["id"]

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

    def test_p1_should_update_label_with_correct_values_and_name_with_special_characters_and_numbers(
            self,
    ) -> None:
        label_name: str = get_all_characters_set_in_random_order()
        label_color: Color = pick_random_enum(Color)

        payload: PutUpdateLabelPayload = PutUpdateLabelPayload(name=label_name, color=label_color.value)

        # PUT
        response_put: Response = put_update_label(self.label_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateLabelDto = deserialize_and_validate_json(response_put, PutUpdateLabelDto)
        expected_response_put_dto: PutUpdateLabelDto = (
            PutUpdateLabelExpected.base()
            .with_id(response_put_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(label_color)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p2_should_update_label_when_name_have_one_character(self) -> None:
        label_name: str = get_random_single_char_alphanumeric()
        label_color: Color = pick_random_enum(Color)

        payload: PutUpdateLabelPayload = PutUpdateLabelPayload(name=label_name, color=label_color.value)

        # PUT
        response_put: Response = put_update_label(self.label_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateLabelDto = deserialize_and_validate_json(response_put, PutUpdateLabelDto)
        expected_response_put_dto: PutUpdateLabelDto = (
            PutUpdateLabelExpected.base()
            .with_id(response_put_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(label_color)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p3_should_update_label_when_name_and_color_are_missing(self) -> None:
        # GET (Get current status of {LABEL})
        response_get: Response = get_get_label(self.label_id)
        assert response_get.status_code == 200
        response_get_dto: GetLabelDto = deserialize_and_validate_json_with_business_rules(response_get, GetLabelDto)
        # PUT
        response_put: Response = put_update_label(self.label_id, None)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateLabelDto = deserialize_and_validate_json(response_put, PutUpdateLabelDto)
        compare_objects(response_put_dto, response_get_dto)
        # GET
        validate_get_against_put(response_put_dto)

    @pytest.mark.flaky
    @pytest.mark.skip(
        reason="Flaky test – Sometimes fields become empty/null, sometimes they are not changed at all"
    )
    def test_p5_should_update_label_when_name_and_color_are_empty_string(self) -> None:
        # NOTE: When we insert empty strings directly as parameters, REST Assured ignores them. When we
        # insert them via variables, it does not. (NOTE FOR ME: kept for fidelity - may not translate 1:1
        # to `requests`' query-param handling, but this test is skipped/flaky either way.)

        label_name: str = ""
        label_color: str = ""

        payload: PutUpdateLabelPayload = PutUpdateLabelPayload(name=label_name, color=label_color)

        # GET (We need to retrieve the current state of the label)
        response_get: Response = get_get_label(self.label_id)
        assert response_get.status_code == 200
        response_get_dto: GetLabelDto = deserialize_and_validate_json_with_business_rules(response_get, GetLabelDto)
        # PUT
        response_put: Response = put_update_label(self.label_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateLabelDto = deserialize_and_validate_json(response_put, PutUpdateLabelDto)
        # IF DATA NOT CHANGE (Except label {id})
        response_get_dto.id = response_put_dto.id
        # IF DATA CHANGE
        expected_response_put_dto: PutUpdateLabelDto = (
            PutUpdateLabelExpected.base()
            .with_id(response_put_dto.id)
            .with_board_id(self.board_id)
            .with_name(label_name)
            .with_color(None)
            .build()
        )
        assert_satisfies_any_of(
            response_put_dto,
            lambda dto: compare_objects(dto, expected_response_put_dto),  # IF DATA CHANGE
            lambda dto: compare_objects(dto, response_get_dto),  # IF DATA NOT CHANGE (Except label {id})
        )
        # GET
        response_get_after_put: Response = get_get_label(self.label_id)
        assert response_get_after_put.status_code == 200
        # NOTE FOR ME: Ported 1:1 - the Java original re-deserializes the STALE `responseGet` here instead
        # of `responseGetAfterPut`. Looks like a copy-paste bug upstream, but since this whole test is
        # @Disabled/skipped (flaky), it has no practical effect. Flagging for Bartłomiej, not silently fixed.
        response_get_dto_after_put: GetLabelDto = deserialize_and_validate_json_with_business_rules(
            response_get, GetLabelDto
        )
        assert_satisfies_any_of(
            response_get_dto_after_put,
            lambda dto: compare_objects(dto, expected_response_put_dto),  # IF DATA CHANGE
            lambda dto: compare_objects(dto, response_get_dto),  # IF DATA NOT CHANGE (Except label {id})
        )

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # --
    # id
    # --

    def test_n3_should_not_update_label_with_non_existent_id(self) -> None:
        # ARRANGE
        label_id: str = "999999999999999999999999"
        # ACT
        response_put: Response = put_update_label(label_id, None)
        # ASSERT
        assert response_put.status_code == 404
        assert response_put.text == "The requested resource was not found."

    def test_n4_should_not_update_label_with_incorrect_id(self) -> None:
        # ARRANGE
        label_id: str = "Kek123"
        # ACT
        response_put: Response = put_update_label(label_id, None)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid id"

    # -----
    # color
    # -----

    def test_n1_should_not_update_label_when_label_color_is_incorrect(self) -> None:
        # ARRANGE
        # NOTE FOR ME: Ported 1:1 - the Java original passes `boardId` here instead of `labelId`. Looks like
        # a copy-paste bug upstream, but it happens to still exercise the "invalid color" validation (which
        # runs before/regardless of the id lookup), so the assertion passes either way. Flagging for
        # Bartłomiej rather than silently fixing it.
        payload: PutUpdateLabelPayload = PutUpdateLabelPayload(color="N1KeK123")
        # ACT
        response_put: Response = put_update_label(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, EXPECTED_PUT_LABEL_RESPONSE_INVALID_COLOR)

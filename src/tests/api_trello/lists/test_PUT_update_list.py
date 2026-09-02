from collections.abc import Generator
from typing import Optional

import pytest
from requests import Response

from dto.lists.GET_get_list_dto import GetListDto
from dto.lists.list_base_dto import ListBaseDto
from dto.lists.POST_create_new_list_dto import PostCreateNewListDto
from dto.lists.PUT_update_list_dto import PutUpdateListDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.lists.GET_get_list_endpoint import get_get_list
from endpoints.lists.POST_create_new_list_endpoint import post_create_new_list
from endpoints.lists.PUT_update_list_endpoint import put_update_list
from expected_responses.lists.PUT_update_list_expected import (
    PutUpdateListExpected,
    EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_ID,
    EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_NAME,
    EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_BOARD_ID,
    EXPECTED_PUT_UPDATE_LIST_RESPONSE_BOARD_NOT_FOUND,
    EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_POSITION,
)
from payloads.lists.PUT_update_list_payload import PutUpdateListPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import (
    deserialize_and_validate_json,
    deserialize_and_validate_json_with_business_rules,
)
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.lists.POST_create_new_list_utils import generate_random_list_name
from utils_tests.lists.PUT_update_list_utils import validate_get_against_put


class TestPutUpdateList(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: str
    # LIST – COMMON
    list_id: str
    # LIST – POST | Some variables are intentionally taken from POST into the expected response, to check
    # whether PUT accidentally changed them when it wasn't supposed to.
    response_post_dto: PostCreateNewListDto

    # NOTE FOR ME: Java also declares `listName`/`listClosed`/`listPosAsLong`/`listPosAsString`/
    # `listSubscribed`/`boardIdN` as class fields, but (same as in the labels/board-list tests) no test ever
    # reads a value set by a previous test - kept as plain locals here.

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    @pytest.fixture(scope="class", autouse=True)
    def setup_create_board_and_list(self, request) -> Generator[None, None, None]:

        # ----------
        # BEFORE ALL
        # ----------

        # BOARD
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        request.cls.board_id = response_post.json()["id"]
        # LIST
        response_post = post_create_new_list(request.cls.board_id, generate_random_list_name(), None)
        assert response_post.status_code == 200
        response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(response_post, PostCreateNewListDto)
        request.cls.response_post_dto = response_post_dto
        request.cls.list_id = response_post_dto.id

        yield

        # ---------
        # AFTER ALL
        # ---------

        response_delete: Response = delete_delete_board(request.cls.board_id)
        assert response_delete.status_code == 200
        request.cls.board_id = None
        request.cls.list_id = None

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_update_list_where_name_special_characters_and_numbers_closed_true_subscribed_true(
            self,
    ) -> None:
        list_name: str = get_all_characters_set_in_random_order()
        list_closed: bool = True
        list_subscribed: bool = True

        payload: PutUpdateListPayload = PutUpdateListPayload(
            name=list_name,
            closed=list_closed,
            subscribed=list_subscribed,
        )

        # GET (Get current status of {LIST})
        response_get: Response = get_get_list(self.list_id)
        assert response_get.status_code == 200
        response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(response_get, GetListDto)
        # PUT
        response_put: Response = put_update_list(self.list_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
        expected_response_put_dto: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(self.list_id)
            .with_name(list_name)
            .with_closed(list_closed)
            .with_board_id(self.board_id)
            .with_pos(response_get_dto.pos)
            .with_subscribed(list_subscribed)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p2_should_update_list_where_name_one_character_and_closed_false_subscribed_false_pos_null(
            self,
    ) -> None:
        list_name: str = get_random_single_char_alphanumeric()
        list_closed: bool = False
        list_pos_as_long: Optional[int] = None
        list_subscribed: bool = False

        payload: PutUpdateListPayload = PutUpdateListPayload(
            name=list_name,
            closed=list_closed,
            pos=list_pos_as_long,
            subscribed=list_subscribed,
        )

        # GET (Get current status of {LIST})
        response_get: Response = get_get_list(self.list_id)
        assert response_get.status_code == 200
        response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(response_get, GetListDto)
        # PUT
        response_put: Response = put_update_list(self.list_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
        expected_response_put_dto: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(self.list_id)
            .with_name(list_name)
            .with_closed(list_closed)
            .with_board_id(self.board_id)
            .with_pos(response_get_dto.pos)
            .with_subscribed(list_subscribed)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p3_should_update_list_where_name_missing_closed_missing_pos_empty_string_subscribed_missing(
            self,
    ) -> None:
        # NOTE:
        # FLAKY TEST
        # REMEMBER: The "pos" field (ListBaseDto.FIELD_POS) is intentionally ignored during comparison.
        # This test uncovered odd behavior: if the first PUT request changes something on the list but not
        # its "pos", or if we try to change "pos" to something that shouldn't change it (like null or an
        # empty string), the original "pos" value still changes anyway.

        list_pos_as_string: str = ""

        payload: PutUpdateListPayload = PutUpdateListPayload(pos=list_pos_as_string)

        # GET (Get current status of {LIST})
        response_get: Response = get_get_list(self.list_id)
        assert response_get.status_code == 200
        response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(response_get, GetListDto)
        # PUT
        response_put: Response = put_update_list(self.list_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
        expected_response_put_dto: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(self.list_id)
            .with_name(response_get_dto.name)
            .with_closed(response_get_dto.closed)
            .with_color(None)
            .with_board_id(self.board_id)
            .with_pos(response_get_dto.pos)
            .with_subscribed(None)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto, ListBaseDto.FIELD_POS)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p5_should_update_three_lists_with_pos_top_bottom_and_number(self) -> None:
        # -------
        # ARRANGE
        # -------

        # POST
        # {LIST 1} was created in the class fixture (BEFORE ALL) | Base list, the others' positions are
        # checked against it
        list_name_2: str = generate_random_list_name()
        list_name_3: str = generate_random_list_name()
        list_name_4: str = generate_random_list_name()
        # PUT
        list_pos_2: str = "top"
        list_pos_3: str = "bottom"

        # NOTE FOR ME:
        # Java hardcodes listPos4 = 140737488322560L, assuming it will always be lower than the base
        # list's (self.response_post_dto) auto-assigned pos. Trello assigns a default pos near 2^47
        # (140737488355328) with a small random jitter, so that assumption is flaky by design - the
        # hardcoded constant sometimes ends up HIGHER than self.response_post_dto.pos, making the
        # "numeric pos should be before list 1" assertion fail at random. Fixed here by deriving
        # list_pos_4 from the actually observed self.response_post_dto.pos, guaranteeing it is always
        # lower, regardless of Trello's jitter.
        list_pos_4: int = self.response_post_dto.pos - 50000

        payload_2: PutUpdateListPayload = PutUpdateListPayload(pos=list_pos_2)
        payload_3: PutUpdateListPayload = PutUpdateListPayload(pos=list_pos_3)
        payload_4: PutUpdateListPayload = PutUpdateListPayload(pos=list_pos_4)

        # ---
        # ACT
        # ---

        # POST (Add {LIST 2})
        response_post_2: Response = post_create_new_list(self.board_id, list_name_2, None)
        assert response_post_2.status_code == 200
        response_post_dto_2: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_2, PostCreateNewListDto
        )
        list_id_2: str = response_post_dto_2.id

        # POST (Add {LIST 3})
        response_post_3: Response = post_create_new_list(self.board_id, list_name_3, None)
        assert response_post_3.status_code == 200
        response_post_dto_3: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_3, PostCreateNewListDto
        )
        list_id_3: str = response_post_dto_3.id

        # POST (Add {LIST 4})
        response_post_4: Response = post_create_new_list(self.board_id, list_name_4, None)
        assert response_post_4.status_code == 200
        response_post_dto_4: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_4, PostCreateNewListDto
        )
        list_id_4: str = response_post_dto_4.id

        # PUT (Edit {LIST 2} -> POS: top)
        response_put_2: Response = put_update_list(list_id_2, payload_2)
        assert response_put_2.status_code == 200
        response_put_dto_2: PutUpdateListDto = deserialize_and_validate_json(response_put_2, PutUpdateListDto)
        response_put_pos_2: int = response_put_dto_2.pos
        expected_response_put_dto_2: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(list_id_2)
            .with_name(response_post_dto_2.name)
            .with_closed(response_post_dto_2.closed)
            .with_color(None)
            .with_board_id(self.board_id)
            .with_pos(response_put_pos_2)
            .with_subscribed(None)
            .build()
        )
        compare_objects(response_put_dto_2, expected_response_put_dto_2)
        # GET
        validate_get_against_put(response_put_dto_2)

        # PUT (Edit {LIST 3} -> POS: bottom)
        response_put_3: Response = put_update_list(list_id_3, payload_3)
        assert response_put_3.status_code == 200
        response_put_dto_3: PutUpdateListDto = deserialize_and_validate_json(response_put_3, PutUpdateListDto)
        response_put_pos_3: int = response_put_dto_3.pos
        expected_response_put_dto_3: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(list_id_3)
            .with_name(response_post_dto_3.name)
            .with_closed(response_post_dto_3.closed)
            .with_color(None)
            .with_board_id(self.board_id)
            .with_pos(response_put_pos_3)
            .with_subscribed(None)
            .build()
        )
        compare_objects(response_put_dto_3, expected_response_put_dto_3)
        # GET
        validate_get_against_put(response_put_dto_3)

        # PUT (Edit {LIST 4} -> POS: 140737488322560)
        response_put_4: Response = put_update_list(list_id_4, payload_4)
        assert response_put_4.status_code == 200
        response_put_dto_4: PutUpdateListDto = deserialize_and_validate_json(response_put_4, PutUpdateListDto)
        response_put_pos_4: int = response_put_dto_4.pos
        expected_response_put_dto_4: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(list_id_4)
            .with_name(response_post_dto_4.name)
            .with_closed(response_post_dto_4.closed)
            .with_color(None)
            .with_board_id(self.board_id)
            .with_pos(response_put_pos_4)
            .with_subscribed(None)
            .build()
        )
        compare_objects(response_put_dto_4, expected_response_put_dto_4)
        # GET
        validate_get_against_put(response_put_dto_4)

        # ------
        # ASSERT
        # ------

        # POSITION VALIDATION
        assert response_put_pos_2 < self.response_post_dto.pos, (
            'The list with the "top" position should be higher (i.e. have a lower numerical value) '
            "than the first list."
        )
        assert response_put_pos_3 > self.response_post_dto.pos, (
            'The list with the "bottom" position should be lower (i.e. have a higher numerical value) '
            "than the first list."
        )
        assert response_put_pos_4 < self.response_post_dto.pos, (
            'The list with the "numeric" item should be higher (i.e. have a lower numerical value) '
            "than the first list."
        )

    def test_p6_should_update_list_by_moving_it_to_another_board(self) -> None:
        # NOTE:
        # FLAKY TEST
        # REMEMBER: The "pos" field (ListBaseDto.FIELD_POS) is intentionally ignored during comparison.
        # This test uncovered odd behavior: if the first PUT request changes something on the list but not
        # its "pos", or if we try to change "pos" to something that shouldn't change it (like null or an
        # empty string), the original "pos" value still changes anyway.

        # POST (Add {BOARD 2})
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        board_id_2: str = response_post.json()["id"]
        try:
            # POST (Add {LIST 2} into {BOARD 1} - so the list used in other tests doesn't get moved)
            response_post = post_create_new_list(self.board_id, generate_random_list_name(), None)
            assert response_post.status_code == 200
            response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(
                response_post, PostCreateNewListDto
            )
            list_id_2: str = response_post_dto.id

            # PUT (Move {LIST 2} from {BOARD 1} to {BOARD 2})
            payload: PutUpdateListPayload = PutUpdateListPayload(id_board=board_id_2)

            response_put: Response = put_update_list(list_id_2, payload)
            assert response_put.status_code == 200
            response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
            expected_response_put_dto: PutUpdateListDto = (
                PutUpdateListExpected.base()
                .with_id(list_id_2)
                .with_name(response_post_dto.name)
                .with_closed(response_post_dto.closed)
                .with_color(response_post_dto.color)
                .with_board_id(board_id_2)
                .with_pos(response_post_dto.pos)
                .with_subscribed(None)
                .build()
            )
            compare_objects(response_put_dto, expected_response_put_dto, ListBaseDto.FIELD_POS)
            # GET
            validate_get_against_put(response_put_dto)
        finally:
            # DELETE (Delete {BOARD 2})
            if board_id_2 is not None:
                # NOTE FOR ME: Java's `catch (Exception e)` here does NOT swallow assertion failures,
                # because AssertJ's AssertionError extends java.lang.Error, not Exception. To match that
                # 1:1 in Python (where AssertionError IS an Exception subclass), the assertion failure is
                # explicitly re-raised, and only other/unexpected exceptions are logged and suppressed.
                try:
                    response_delete: Response = delete_delete_board(board_id_2)
                    assert response_delete.status_code == 200
                except AssertionError:
                    raise
                except Exception as e:
                    print(f"Failed to delete {{BOARD 2}}: {board_id_2}")
                    print(e)

    def test_p7_should_update_list_when_id_board_null(self) -> None:
        list_name: str = generate_random_list_name()
        board_id_2: Optional[str] = None

        payload: PutUpdateListPayload = PutUpdateListPayload(name=list_name, id_board=board_id_2)

        # GET (Get current status of {LIST})
        response_get: Response = get_get_list(self.list_id)
        assert response_get.status_code == 200
        response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(response_get, GetListDto)
        # PUT
        response_put: Response = put_update_list(self.list_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
        expected_response_put_dto: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(self.list_id)
            .with_name(list_name)
            .with_board_id(self.board_id)
            .with_pos(response_get_dto.pos)
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p8_should_update_list_when_pos_number_as_string(self) -> None:
        list_pos_as_string: str = "140737488322560"

        payload: PutUpdateListPayload = PutUpdateListPayload(pos=list_pos_as_string)

        # GET (Get current status of {LIST})
        response_get: Response = get_get_list(self.list_id)
        assert response_get.status_code == 200
        response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(response_get, GetListDto)
        # PUT
        response_put: Response = put_update_list(self.list_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PutUpdateListDto = deserialize_and_validate_json(response_put, PutUpdateListDto)
        expected_response_put_dto: PutUpdateListDto = (
            PutUpdateListExpected.base()
            .with_id(self.list_id)
            .with_name(response_get_dto.name)
            .with_board_id(self.board_id)
            .with_pos(int(list_pos_as_string))
            .build()
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # --
    # id
    # --

    @pytest.mark.parametrize(
        "test_id, test_description, list_id",
        [
            pytest.param("N1", "should_not_update_list_when_id_non_existent", "99", id="N1"),
            pytest.param("N2", "should_not_update_list_when_id_incorrect", "KeK", id="N2"),
        ],
    )
    def test_should_not_update_list_with_invalid_id(
            self, test_id: str, test_description: str, list_id: str
    ) -> None:
        # ACT
        response_put: Response = put_update_list(list_id, None)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_ID

    # ----
    # name
    # ----

    def test_n3_should_not_update_list_when_name_empty_string(self) -> None:
        # ARRANGE
        list_name: str = ""
        payload: PutUpdateListPayload = PutUpdateListPayload(name=list_name)
        # ACT
        response_put: Response = put_update_list(self.list_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_NAME)

    # -------
    # idBoard
    # -------

    @pytest.mark.parametrize(
        "test_id, test_description, id_board",
        [
            pytest.param("N4", "should_not_update_list_when_id_board_empty_string", "", id="N4"),
            pytest.param("N6", "should_not_update_list_when_id_board_incorrect", "KeK", id="N6"),
        ],
    )
    def test_should_not_update_list_with_invalid_board_id(
            self, test_id: str, test_description: str, id_board: str
    ) -> None:
        # ARRANGE
        payload: PutUpdateListPayload = PutUpdateListPayload(name=generate_random_list_name(), id_board=id_board)
        # ACT
        response_put: Response = put_update_list(self.list_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_BOARD_ID)

    def test_n5_should_not_update_list_when_id_board_non_existent(self) -> None:
        # ARRANGE
        board_id_n: str = "691db99a4e5a030526097e00"
        payload: PutUpdateListPayload = PutUpdateListPayload(name=generate_random_list_name(), id_board=board_id_n)
        # ACT
        response_put: Response = put_update_list(self.list_id, payload)
        # ASSERT
        assert response_put.status_code == 404
        compare_response_with_json(response_put, EXPECTED_PUT_UPDATE_LIST_RESPONSE_BOARD_NOT_FOUND)

    # ---
    # pos
    # ---

    def test_n7_should_not_update_list_when_pos_incorrect(self) -> None:
        # ARRANGE
        list_pos_as_string: str = "KeK 123"
        payload: PutUpdateListPayload = PutUpdateListPayload(
            name=generate_random_list_name(), pos=list_pos_as_string
        )
        # ACT
        response_put: Response = put_update_list(self.list_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_POSITION)

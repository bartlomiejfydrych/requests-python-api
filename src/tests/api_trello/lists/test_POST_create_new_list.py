from typing import Optional

import pytest
from requests import Response

from dto.lists.POST_create_new_list_dto import PostCreateNewListDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.lists.POST_create_new_list_endpoint import (
    post_create_new_list,
    post_create_new_list_with_any_params,
)
from expected_responses.lists.POST_create_new_list_expected import (
    PostCreateNewListExpected,
    EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_NAME,
    EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_BOARD,
    EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_LIST_SOURCE,
    EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_POS,
)
from payloads.lists.POST_create_new_list_payload import PostCreateNewListPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.lists.POST_create_new_list_utils import generate_random_list_name, validate_get_against_post


class TestPostCreateNewList(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    # BOARD
    board_id: Optional[str] = None

    # NOTE FOR ME: Java also declares `listName`/`listIdListSource`/`listPos` as class fields, but (same as
    # in the labels tests) no test ever reads a value set by a previous test - kept as plain locals here.

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    @pytest.fixture(scope="class", autouse=True)
    def setup_create_board(self, request) -> None:
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
        if request.cls.board_id is not None:
            response_delete: Response = delete_delete_board(request.cls.board_id)
            assert response_delete.status_code == 200
            request.cls.board_id = None

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

    def test_p1_should_create_new_list_where_name_is_with_special_characters_and_numbers(self) -> None:
        list_name: str = get_all_characters_set_in_random_order()

        # POST
        response_post: Response = post_create_new_list(self.board_id, list_name, None)
        assert response_post.status_code == 200
        response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(response_post, PostCreateNewListDto)
        expected_response_post_dto: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto.id)
            .with_name(list_name)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto.pos)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p2_should_create_new_list_where_name_have_only_one_character_and_other_parameters_are_null(
            self,
    ) -> None:
        list_name: str = get_random_single_char_alphanumeric()
        list_id_list_source: Optional[str] = None
        list_pos: Optional[str] = None

        payload: PostCreateNewListPayload = PostCreateNewListPayload(
            id_list_source=list_id_list_source,
            pos=list_pos,
        )

        # POST
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        assert response_post.status_code == 200
        response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(response_post, PostCreateNewListDto)
        expected_response_post_dto: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto.id)
            .with_name(list_name)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto.pos)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p3_should_create_new_list_with_correct_id_list_source(self) -> None:
        list_name_1: str = generate_random_list_name()
        list_name_2: str = generate_random_list_name()

        # POST (Add {LIST 1})
        response_post_1: Response = post_create_new_list(self.board_id, list_name_1, None)
        assert response_post_1.status_code == 200
        response_post_dto_1: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_1, PostCreateNewListDto
        )

        # POST (Add {LIST 2} and assign it {idListSource} from {LIST 1})
        payload: PostCreateNewListPayload = PostCreateNewListPayload(id_list_source=response_post_dto_1.id)
        response_post_2: Response = post_create_new_list(self.board_id, list_name_2, payload)
        assert response_post_2.status_code == 200
        response_post_dto_2: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_2, PostCreateNewListDto
        )
        expected_response_post_dto_2: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto_2.id)
            .with_name(list_name_2)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto_2.pos)
            .build()
        )
        compare_objects(response_post_dto_2, expected_response_post_dto_2)
        # GET
        validate_get_against_post(response_post_dto_2)

    def test_p4_should_create_three_new_lists_with_pos_top_bottom_and_number(self) -> None:
        # -------
        # ARRANGE
        # -------

        list_name_1: str = generate_random_list_name()  # Base list, the others' positions are checked against it
        list_name_2: str = generate_random_list_name()
        list_name_3: str = generate_random_list_name()
        list_name_4: str = generate_random_list_name()
        list_pos_2: str = "top"
        list_pos_3: str = "bottom"
        list_pos_4: int = 140737488322560

        payload_2: PostCreateNewListPayload = PostCreateNewListPayload(pos=list_pos_2)
        payload_3: PostCreateNewListPayload = PostCreateNewListPayload(pos=list_pos_3)
        payload_4: PostCreateNewListPayload = PostCreateNewListPayload(pos=list_pos_4)

        # ---
        # ACT
        # ---

        # POST (Add {LIST 1})
        response_post_1: Response = post_create_new_list(self.board_id, list_name_1, None)
        assert response_post_1.status_code == 200
        response_post_dto_1: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_1, PostCreateNewListDto
        )
        response_post_pos_1: int = response_post_dto_1.pos

        # POST (Add {LIST 2})
        response_post_2: Response = post_create_new_list(self.board_id, list_name_2, payload_2)
        assert response_post_2.status_code == 200
        response_post_dto_2: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_2, PostCreateNewListDto
        )
        response_post_pos_2: int = response_post_dto_2.pos
        expected_response_post_dto_2: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto_2.id)
            .with_name(list_name_2)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto_2.pos)
            .build()
        )
        compare_objects(response_post_dto_2, expected_response_post_dto_2)
        # GET
        validate_get_against_post(response_post_dto_2)

        # POST (Add {LIST 3})
        response_post_3: Response = post_create_new_list(self.board_id, list_name_3, payload_3)
        assert response_post_3.status_code == 200
        response_post_dto_3: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_3, PostCreateNewListDto
        )
        response_post_pos_3: int = response_post_dto_3.pos
        expected_response_post_dto_3: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto_3.id)
            .with_name(list_name_3)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto_3.pos)
            .build()
        )
        compare_objects(response_post_dto_3, expected_response_post_dto_3)
        # GET
        validate_get_against_post(response_post_dto_3)

        # POST (Add {LIST 4})
        response_post_4: Response = post_create_new_list(self.board_id, list_name_4, payload_4)
        assert response_post_4.status_code == 200
        response_post_dto_4: PostCreateNewListDto = deserialize_and_validate_json(
            response_post_4, PostCreateNewListDto
        )
        response_post_pos_4: int = response_post_dto_4.pos
        expected_response_post_dto_4: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto_4.id)
            .with_name(list_name_4)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto_4.pos)
            .build()
        )
        compare_objects(response_post_dto_4, expected_response_post_dto_4)
        # GET
        validate_get_against_post(response_post_dto_4)

        # ------
        # ASSERT
        # ------

        # POSITION VALIDATION
        assert response_post_pos_2 < response_post_pos_1, (
            'The list with the "top" position should be higher (i.e. have a lower numerical value) '
            "than the first list."
        )
        assert response_post_pos_3 > response_post_pos_1, (
            'The list with the "bottom" position should be lower (i.e. have a higher numerical value) '
            "than the first list."
        )
        assert response_post_pos_4 < response_post_pos_1, (
            'The list with the "numeric" item should be higher (i.e. have a lower numerical value) '
            "than the first list."
        )

    def test_p5_should_create_new_list_where_other_parameters_are_empty_strings(self) -> None:
        list_name: str = generate_random_list_name()
        list_id_list_source: str = ""
        list_pos: str = ""

        payload: PostCreateNewListPayload = PostCreateNewListPayload(
            id_list_source=list_id_list_source,
            pos=list_pos,
        )

        # POST
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        assert response_post.status_code == 200
        response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(response_post, PostCreateNewListDto)
        expected_response_post_dto: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto.id)
            .with_name(list_name)
            .with_board_id(self.board_id)
            .with_pos(response_post_dto.pos)
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p6_should_create_new_list_when_pos_is_number_as_string(self) -> None:
        # NOTE: According to the documentation, the specific position of a list should be of type Number.
        # A String value will also work.

        list_name: str = generate_random_list_name()
        list_pos: str = "140737488326656"

        payload: PostCreateNewListPayload = PostCreateNewListPayload(pos=list_pos)

        # POST
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        assert response_post.status_code == 200
        response_post_dto: PostCreateNewListDto = deserialize_and_validate_json(response_post, PostCreateNewListDto)
        expected_response_post_dto: PostCreateNewListDto = (
            PostCreateNewListExpected.base()
            .with_id(response_post_dto.id)
            .with_name(list_name)
            .with_board_id(self.board_id)
            .with_pos(int(list_pos))
            .build()
        )
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # ----
    # name
    # ----

    def test_n1_should_not_create_new_list_when_name_is_missing(self) -> None:
        # ARRANGE
        payload: PostCreateNewListPayload = PostCreateNewListPayload(id_board=self.board_id)
        # ACT
        response_post: Response = post_create_new_list_with_any_params(payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_NAME)

    def test_n3_should_not_create_new_list_when_name_is_empty_string(self) -> None:
        # ARRANGE
        list_name: str = ""
        # ACT
        response_post: Response = post_create_new_list(self.board_id, list_name, None)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_NAME)

    # -------
    # idBoard
    # -------

    def test_n4_should_not_create_new_list_when_id_board_is_missing(self) -> None:
        # ARRANGE
        payload: PostCreateNewListPayload = PostCreateNewListPayload(name=generate_random_list_name())
        # ACT
        response_post: Response = post_create_new_list_with_any_params(payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_BOARD

    @pytest.mark.parametrize(
        "test_id, test_description, id_board",
        [
            pytest.param("N6", "should_not_create_new_list_when_id_board_is_empty_string", "", id="N6"),
            pytest.param("N8", "should_not_create_new_list_when_id_board_is_incorrect", "KeK 123", id="N8"),
        ],
    )
    def test_should_not_create_new_list_with_invalid_board_id(
            self, test_id: str, test_description: str, id_board: str
    ) -> None:
        # ARRANGE
        list_name: str = generate_random_list_name()
        # ACT
        response_post: Response = post_create_new_list(id_board, list_name, None)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_BOARD

    def test_n7_should_not_create_new_list_when_id_board_is_non_existent(self) -> None:
        # ARRANGE
        id_board: str = "999999999999999999999999"
        list_name: str = generate_random_list_name()
        # ACT
        response_post: Response = post_create_new_list(id_board, list_name, None)
        # ASSERT
        assert response_post.status_code == 401
        assert response_post.text == f"unauthorized board list requested {id_board}"

    # ------------
    # idListSource
    # ------------

    def test_n9_should_not_create_new_list_when_id_list_source_is_non_existent(self) -> None:
        # ARRANGE
        list_name: str = generate_random_list_name()
        list_id_list_source: str = "999999999999999999999999"

        payload: PostCreateNewListPayload = PostCreateNewListPayload(id_list_source=list_id_list_source)
        # ACT
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        # ASSERT
        assert response_post.status_code == 404
        assert response_post.text == "Source list not found"

    def test_n10_should_not_create_new_list_when_id_list_source_is_incorrect(self) -> None:
        # ARRANGE
        list_name: str = generate_random_list_name()
        list_id_list_source: str = "KeK 123"

        payload: PostCreateNewListPayload = PostCreateNewListPayload(id_list_source=list_id_list_source)
        # ACT
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_LIST_SOURCE)

    # ---
    # pos
    # ---

    def test_n11_should_not_create_new_list_when_pos_is_incorrect(self) -> None:
        # ARRANGE
        list_name: str = generate_random_list_name()
        list_pos: str = "Kek 123"

        payload: PostCreateNewListPayload = PostCreateNewListPayload(pos=list_pos)
        # ACT
        response_post: Response = post_create_new_list(self.board_id, list_name, payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_POS)

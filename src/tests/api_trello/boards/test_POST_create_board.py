from typing import Optional

import pytest
from requests import Response

from configuration.config import get_trello_id
from dto.boards.POST_create_board_dto import POST_CreateBoardDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.POST_create_board_endpoint import post_create_board, post_create_board_missing_required_parameters
from expected_responses.boards.POST_create_board_expected import (
    P1_EXPECTED_POST_BOARD_RESPONSE,
    P2_EXPECTED_POST_BOARD_RESPONSE,
    P3_EXPECTED_POST_BOARD_RESPONSE,
    P5_EXPECTED_POST_BOARD_RESPONSE,
    P1_EXPECTED_POST_BOARD_RESPONSE_INVALID_NAME,
)
from payloads.boards.POST_create_board_payload import PostCreateBoardPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_random import pick_random
from utils_tests.boards.POST_create_board_utils import (
    prepare_expected_response_post,
    validate_get_against_post,
    generate_random_board_name,
    generate_random_desc,
)


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

    def test_p2_should_create_board_when_most_parameters_are_given(self) -> None:
        board_name: str = "F"

        payload: PostCreateBoardPayload = PostCreateBoardPayload(
            default_labels=True,
            default_lists=True,
            desc=(
                "!\"#$%&\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
                "ęĘóÓąĄśŚłŁżŻźŹćĆńŃ"
            ),
            id_organization=self.trello_id,
            keep_from_source="none",
            power_ups="all",
            prefs_permission_level="private",
            prefs_voting="disabled",
            prefs_comments="members",
            prefs_invitations="members",
            prefs_self_join=True,
            prefs_card_covers=True,
            prefs_background="blue",
            prefs_card_aging="regular",
        )

        # POST
        response_post: Response = post_create_board(board_name, payload)
        assert response_post.status_code == 200
        self.board_id = response_post.json()["id"]
        response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
        expected_response_post_dto: POST_CreateBoardDto = prepare_expected_response_post(
            P2_EXPECTED_POST_BOARD_RESPONSE, response_post_dto, board_name
        )
        expected_response_post_dto.id_organization = self.trello_id
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p3_should_create_board_when_most_parameters_are_given(self) -> None:
        board_name: str = generate_random_board_name()
        desc: str = generate_random_desc()

        payload: PostCreateBoardPayload = PostCreateBoardPayload(
            default_labels=False,
            default_lists=False,
            desc=desc,
            keep_from_source="cards",
            power_ups="calendar",
            prefs_permission_level="org",
            prefs_voting="members",
            prefs_comments="observers",
            prefs_invitations="admins",
            prefs_self_join=False,
            prefs_card_covers=False,
            prefs_background="orange",
            prefs_card_aging="pirate",
        )

        # POST
        response_post: Response = post_create_board(board_name, payload)
        assert response_post.status_code == 200
        self.board_id = response_post.json()["id"]
        response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
        expected_response_post_dto: POST_CreateBoardDto = prepare_expected_response_post(
            P3_EXPECTED_POST_BOARD_RESPONSE, response_post_dto, board_name
        )
        expected_response_post_dto.desc = desc
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    def test_p5_should_create_board_with_remaining_random_parameters(self) -> None:
        board_name: str = generate_random_board_name()
        power_ups: str = pick_random("cardAging", "recap", "voting")
        prefs_voting: str = pick_random("observers", "org", "public")
        prefs_comments: str = pick_random("disabled", "org", "public")
        prefs_background: str = pick_random("green", "red", "purple", "pink", "lime", "sky", "grey")

        # NOTE FOR ME: Java's switch expression -> dict lookup with a default ("blue" if not matched)
        prefs_background_hex_map: dict[str, str] = {
            "green": "#519839",
            "red": "#B04632",
            "purple": "#89609E",
            "pink": "#CD5A91",
            "lime": "#4BBF6B",
            "sky": "#00AECC",
            "grey": "#838C91",
        }
        prefs_background_hex: str = prefs_background_hex_map.get(prefs_background, "#0079BF")  # "blue" if not matched

        payload: PostCreateBoardPayload = PostCreateBoardPayload(
            power_ups=power_ups,
            prefs_permission_level="public",
            prefs_voting=prefs_voting,
            prefs_comments=prefs_comments,
            prefs_background=prefs_background,
        )

        # POST
        response_post: Response = post_create_board(board_name, payload)
        assert response_post.status_code == 200
        self.board_id = response_post.json()["id"]
        response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
        expected_response_post_dto: POST_CreateBoardDto = prepare_expected_response_post(
            P5_EXPECTED_POST_BOARD_RESPONSE, response_post_dto, board_name
        )
        expected_response_post_dto.prefs.voting = prefs_voting
        expected_response_post_dto.prefs.comments = prefs_comments
        expected_response_post_dto.prefs.background = prefs_background
        expected_response_post_dto.prefs.background_color = prefs_background_hex
        expected_response_post_dto.prefs.background_bottom_color = prefs_background_hex
        expected_response_post_dto.prefs.background_top_color = prefs_background_hex
        compare_objects(response_post_dto, expected_response_post_dto)
        # GET
        validate_get_against_post(response_post_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # ----
    # name
    # ----

    @pytest.mark.parametrize(
        "test_id, test_description, name",
        [
            pytest.param("N1", "should_not_create_board_when_name_was_not_given", None, id="N1"),
            pytest.param("N3", "should_not_create_board_when_name_is_empty_string", "", id="N3"),
        ],
    )
    def test_should_not_create_board_with_invalid_name(
            self, test_id: str, test_description: str, name: Optional[str]
    ) -> None:
        # ACT
        if name is None:
            response_post: Response = post_create_board_missing_required_parameters()
        else:
            response_post = post_create_board(name, None)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, P1_EXPECTED_POST_BOARD_RESPONSE_INVALID_NAME)

    # --------------
    # idOrganization
    # --------------

    @pytest.mark.parametrize(
        "test_id, test_description, id_organization",
        [
            pytest.param(
                "N4", "should_not_create_board_when_id_organization_non_exist", "123456789098765432123456", id="N4"
            ),
            pytest.param(
                "N5", "should_not_create_board_when_id_organization_is_incompatible_with_regex", "123abc", id="N5"
            ),
        ],
    )
    def test_should_not_create_board_with_invalid_organization(
            self, test_id: str, test_description: str, id_organization: str
    ) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(id_organization=id_organization)
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 401
        assert response_post.text == "unauthorized org access"

    # -------------
    # idBoardSource
    # -------------

    def test_n6_should_not_create_board_when_id_board_source_non_exist(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(id_board_source="123456789098765432123456")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 404
        assert response_post.text == "source board not found"

    def test_n7_should_not_create_board_when_id_board_source_is_incompatible_with_regex(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
            "message": "Invalid objectId",
            "error": "ERROR"
        }
        """

        payload: PostCreateBoardPayload = PostCreateBoardPayload(id_board_source="123abc")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        compare_response_with_json(response_post, expected_response)

    # ---------------------
    # prefs_permissionLevel
    # ---------------------

    def test_n8_should_not_create_board_when_prefs_permission_level_is_other_string(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(prefs_permission_level="other")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == "invalid value for prefs_permissionLevel"

    # ------------
    # prefs_voting
    # ------------

    def test_n9_should_not_create_board_when_prefs_voting_is_other_string(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(prefs_voting="other")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == "invalid value for prefs_voting"

    # --------------
    # prefs_comments
    # --------------

    def test_n10_should_not_create_board_when_prefs_comments_is_other_string(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(prefs_comments="other")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == "invalid value for prefs_comments"

    # -----------------
    # prefs_invitations
    # -----------------

    def test_n11_should_not_create_board_when_prefs_invitations_is_other_string(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(prefs_invitations="other")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == "invalid value for prefs_invitations"

    # ---------------
    # prefs_cardAging
    # ---------------

    def test_n12_should_not_create_board_when_prefs_card_aging_is_other_string(self) -> None:
        # ARRANGE
        payload: PostCreateBoardPayload = PostCreateBoardPayload(prefs_card_aging="other")
        # ACT
        response_post: Response = post_create_board(generate_random_board_name(), payload)
        # ASSERT
        assert response_post.status_code == 400
        assert response_post.text == "invalid value for prefs_cardAging"

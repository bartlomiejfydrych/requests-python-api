from typing import Optional

import pytest
from pydantic import AnyUrl
from requests import Response

from configuration.config import get_trello_id
from dto.boards.GET_get_board_dto import GET_GetBoardDto
from dto.boards.POST_create_board_dto import POST_CreateBoardDto
from dto.boards.PUT_update_board_dto import PUT_UpdateBoardDto
from endpoints.boards.DEL_delete_board_endpoint import delete_delete_board
from endpoints.boards.GET_get_board_endpoint import get_get_board
from endpoints.boards.POST_create_board_endpoint import post_create_board
from endpoints.boards.PUT_update_board_endpoint import put_update_board
from expected_responses.boards.PUT_update_board_expected import (
    P1_EXPECTED_PUT_BOARD_RESPONSE,
    P4_EXPECTED_PUT_BOARD_RESPONSE,
    P5_EXPECTED_PUT_BOARD_RESPONSE,
)
from payloads.boards.PUT_update_board_payload import PutUpdateBoardPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import (
    deserialize_and_validate_json,
    deserialize_and_validate_json_with_business_rules,
)
from utils.utils_compare import compare_objects, compare_response_with_json
from utils.utils_random import pick_random
from utils.utils_string import get_all_characters_set_in_random_order, get_random_single_char_alphanumeric
from utils_tests.boards.POST_create_board_utils import generate_random_board_name
from utils_tests.boards.PUT_update_board_utils import (
    prepare_expected_response_put,
    validate_get_against_put,
    strip_board_name_from_url,
)


class TestPutUpdateBoard(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    trello_id: str = get_trello_id()
    # BOARD (POST) – changing variables
    board_id: Optional[str] = None
    board_name: Optional[str] = None
    board_url: Optional[AnyUrl] = None
    board_short_url: Optional[AnyUrl] = None

    # ==========================================================================================================
    # SETUP & TEARDOWN
    # ==========================================================================================================

    # NOTE FOR ME: JUnit's @TestInstance(PER_CLASS) + @BeforeAll/@AfterAll on a single shared instance ->
    # pytest's scope="class" fixture. Because pytest creates a FRESH test instance per test method (unlike
    # JUnit's PER_CLASS lifecycle), the shared board must live on the CLASS object itself (request.cls),
    # not on `self` - otherwise the next test method wouldn't see it.

    @pytest.fixture(scope="class", autouse=True)
    def setup_create_board(self, request) -> None:
        # ----------
        # BEFORE ALL
        # ----------
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
        request.cls.board_id = response_post_dto.id
        request.cls.board_name = response_post_dto.name
        request.cls.board_url = response_post_dto.url
        request.cls.board_short_url = response_post_dto.short_url

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

    def test_p1_should_update_board_when_most_string_parameters_have_special_characters_and_booleans_are_true(
            self,
    ) -> None:
        # POST
        board_id: Optional[str] = None
        # PUT
        board_name: str = get_all_characters_set_in_random_order()
        self.__class__.board_name = board_name
        desc: str = get_all_characters_set_in_random_order()

        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(
            name=board_name,
            desc=desc,
            closed=True,  # NOTE: Closed boards cannot edit. Discussed with Trello.
            id_organization=self.trello_id,
            prefs_permission_level="org",
            prefs_self_join=True,
            prefs_card_covers=True,
            prefs_hide_votes=True,
            prefs_invitations="admins",
            prefs_voting="disabled",
            prefs_comments="disabled",
            # prefs_background="blue",  # NOTE: The value "blue" stopped working (500) | Reported:
            # https://ecosystem.atlassian.net/servicedesk/customer/portal/34/ECOHELP-99809?created=true
            prefs_card_aging="regular",
            prefs_calendar_feed_enabled=True,
        )

        # POST (We need to create a separate, independent board because it should not be editable once closed,
        # so this step breaks the rest of the tests.)
        response_post: Response = post_create_board(generate_random_board_name(), None)
        assert response_post.status_code == 200
        try:
            response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(response_post, POST_CreateBoardDto)
            board_id = response_post_dto.id
            post_board_url: AnyUrl = response_post_dto.url
            post_board_short_url: AnyUrl = response_post_dto.short_url
            # PUT
            response_put: Response = put_update_board(board_id, payload)
            assert response_put.status_code == 200
            response_put_dto: PUT_UpdateBoardDto = deserialize_and_validate_json(response_put, PUT_UpdateBoardDto)
            assert response_put_dto.url != post_board_url
            assert strip_board_name_from_url(str(response_put_dto.url)) == strip_board_name_from_url(
                str(post_board_url)
            )
            expected_response_put_dto: PUT_UpdateBoardDto = prepare_expected_response_put(
                P1_EXPECTED_PUT_BOARD_RESPONSE, board_id, board_name, response_put_dto.url, post_board_short_url
            )
            expected_response_put_dto.desc = desc
            expected_response_put_dto.id_organization = self.trello_id
            expected_response_put_dto.organization.memberships[0].last_active = (
                response_put_dto.organization.memberships[0].last_active
            )
            compare_objects(response_put_dto, expected_response_put_dto)
            # GET
            validate_get_against_put(response_put_dto)
        finally:
            # DELETE
            if board_id is not None:
                response_delete: Response = delete_delete_board(board_id)
                assert response_delete.status_code == 200
                board_id = None

    def test_p3_should_update_board_when_all_parameters_are_missing(self) -> None:
        # GET (Get current status of {BOARD})
        response_get: Response = get_get_board(self.board_id)
        assert response_get.status_code == 200
        response_get_dto: GET_GetBoardDto = deserialize_and_validate_json_with_business_rules(
            response_get, GET_GetBoardDto
        )
        # PUT
        response_put: Response = put_update_board(self.board_id, None)
        assert response_put.status_code == 200
        response_put_dto: PUT_UpdateBoardDto = deserialize_and_validate_json(response_put, PUT_UpdateBoardDto)
        compare_objects(response_put_dto, response_get_dto, PUT_UpdateBoardDto.FIELD_ORGANIZATION)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p4_should_update_board_when_name_have_only_one_character_and_booleans_are_false(self) -> None:
        board_name: str = get_random_single_char_alphanumeric()
        self.__class__.board_name = board_name

        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(
            name=board_name,
            closed=False,
            prefs_permission_level="private",
            prefs_self_join=False,
            prefs_card_covers=False,
            prefs_hide_votes=False,
            prefs_invitations="members",
            prefs_voting="members",
            prefs_comments="members",
            prefs_background="orange",
            prefs_card_aging="pirate",
            prefs_calendar_feed_enabled=False,
        )

        # PUT
        response_put: Response = put_update_board(self.board_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PUT_UpdateBoardDto = deserialize_and_validate_json(response_put, PUT_UpdateBoardDto)
        assert response_put_dto.url != self.board_url
        assert strip_board_name_from_url(str(response_put_dto.url)) == strip_board_name_from_url(
            str(self.board_url)
        )
        expected_response_put_dto: PUT_UpdateBoardDto = prepare_expected_response_put(
            P4_EXPECTED_PUT_BOARD_RESPONSE, self.board_id, board_name, response_put_dto.url, self.board_short_url
        )
        expected_response_put_dto.organization.memberships[0].last_active = (
            response_put_dto.organization.memberships[0].last_active
        )
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    def test_p5_should_update_board_when_remaining_parameters_are_provided_randomly(self) -> None:
        prefs_voting: str = pick_random("org", "public")
        prefs_comments: str = pick_random("org", "public")
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

        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(
            prefs_permission_level="public",
            prefs_voting=prefs_voting,
            prefs_comments=prefs_comments,
            prefs_background=prefs_background,
        )

        # PUT
        response_put: Response = put_update_board(self.board_id, payload)
        assert response_put.status_code == 200
        response_put_dto: PUT_UpdateBoardDto = deserialize_and_validate_json(response_put, PUT_UpdateBoardDto)
        expected_response_put_dto: PUT_UpdateBoardDto = prepare_expected_response_put(
            P5_EXPECTED_PUT_BOARD_RESPONSE, self.board_id, self.board_name, self.board_url, self.board_short_url
        )
        expected_response_put_dto.prefs.voting = prefs_voting
        expected_response_put_dto.prefs.comments = prefs_comments
        expected_response_put_dto.prefs.background = prefs_background
        expected_response_put_dto.prefs.background_color = prefs_background_hex
        expected_response_put_dto.prefs.background_bottom_color = prefs_background_hex
        expected_response_put_dto.prefs.background_top_color = prefs_background_hex
        compare_objects(response_put_dto, expected_response_put_dto)
        # GET
        validate_get_against_put(response_put_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    # --
    # id
    # --

    def test_n12_should_not_update_board_with_non_existent_id(self) -> None:
        # ARRANGE
        board_id: str = "999999999999999999999999"
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(name="Board name – negative test")
        # ACT
        response_put: Response = put_update_board(board_id, payload)
        # ASSERT
        assert response_put.status_code == 404
        assert response_put.text == "The requested resource was not found."

    def test_n13_should_not_update_board_with_incorrect_id(self) -> None:
        # ARRANGE
        board_id: str = "Kek123"
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(name="Board name – negative test")
        # ACT
        response_put: Response = put_update_board(board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid id"

    # ----
    # name
    # ----

    def test_n1_should_not_update_board_when_name_is_empty_string(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
            "message": "invalid value for name",
            "error": "ERROR"
        }
        """
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(name="")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, expected_response)

    # ----------
    # subscribed
    # ----------

    @pytest.mark.parametrize(
        "test_id, test_description, subscribed",
        [
            pytest.param(
                "N2", "should_not_update_board_when_subscribed_not_exist", "123456789098765432123456", id="N2"
            ),
            pytest.param(
                "N3", "should_not_update_board_when_subscribed_is_incompatible_with_regex", "123abc", id="N3"
            ),
        ],
    )
    def test_should_not_update_board_with_invalid_subscribed(
            self, test_id: str, test_description: str, subscribed: str
    ) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(subscribed=subscribed)
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for subscribed"

    # --------------
    # idOrganization
    # --------------

    @pytest.mark.parametrize(
        "test_id, test_description, id_organization",
        [
            pytest.param(
                "N4", "should_not_update_board_when_id_organization_not_exist", "123456789098765432123456", id="N4"
            ),
            pytest.param(
                "N5",
                "should_not_update_board_when_id_organization_is_incompatible_with_regex",
                "123abc",
                id="N5",
            ),
        ],
    )
    def test_should_not_update_board_with_invalid_organization(
            self, test_id: str, test_description: str, id_organization: str
    ) -> None:
        # ARRANGE
        expected_response: str = """
        {
            "message": "unauthorized organization access"
        }
        """
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(id_organization=id_organization)
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 401
        compare_response_with_json(response_put, expected_response)

    # ---------------------
    # prefs/permissionLevel
    # ---------------------

    def test_n6_should_not_update_board_when_prefs_permission_level_is_other_string(self) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_permission_level="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for prefs/permissionLevel"

    # -----------------
    # prefs/invitations
    # -----------------

    def test_n7_should_not_update_board_when_prefs_invitations_is_other_string(self) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_invitations="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for prefs/invitations"

    # ------------
    # prefs/voting
    # ------------

    def test_n8_should_not_update_board_when_prefs_voting_is_other_string(self) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_voting="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for prefs/voting"

    # --------------
    # prefs/comments
    # --------------

    def test_n9_should_not_update_board_when_prefs_comments_is_other_string(self) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_comments="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for prefs/comments"

    # ----------------
    # prefs/background
    # ----------------

    def test_n10_should_not_update_board_when_prefs_background_is_other_string(self) -> None:
        # ARRANGE
        expected_response: str = """
        {
            "message": "Invalid background",
            "error": "ERROR"
        }
        """
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_background="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        compare_response_with_json(response_put, expected_response)

    # ---------------
    # prefs/cardAging
    # ---------------

    def test_n11_should_not_update_board_when_prefs_card_aging_is_other_string(self) -> None:
        # ARRANGE
        payload: PutUpdateBoardPayload = PutUpdateBoardPayload(prefs_card_aging="KeK")
        # ACT
        response_put: Response = put_update_board(self.board_id, payload)
        # ASSERT
        assert response_put.status_code == 400
        assert response_put.text == "invalid value for prefs/cardAging"

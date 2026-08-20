from requests import Response

from dto.emoji.GET_list_available_emoji_dto import GetListAvailableEmojiDto
from endpoints.emoji.GET_list_available_emoji_endpoint import get_list_available_emoji
from payloads.emoji.GET_list_available_emoji_payload import GetListAvailableEmojiPayload
from tests.base.test_base import TestBase
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_compare import compare_objects
from utils_tests.emoji.GET_list_available_emoji_utils import get_expected_response_dto


class TestGetListAvailableEmoji(TestBase):
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # ---------------
    # CLASS VARIABLES
    # ---------------

    common_file_name: str = "ExpectedGetListAvailableEmojiResponse.json"

    # ==========================================================================================================
    # POSITIVE TESTS
    # ==========================================================================================================

    def test_p1_should_get_list_available_emoji_when_query_parameters_are_missing(self) -> None:
        # GET
        response_get: Response = get_list_available_emoji(None)
        assert response_get.status_code == 200
        response_get_dto: GetListAvailableEmojiDto = deserialize_and_validate_json(
            response_get, GetListAvailableEmojiDto
        )
        expected_response_get_dto: GetListAvailableEmojiDto = get_expected_response_dto(self.common_file_name)
        compare_objects(response_get_dto, expected_response_get_dto)

    def test_p3_should_get_list_available_emoji_when_spritesheets_is_false(self) -> None:
        payload: GetListAvailableEmojiPayload = GetListAvailableEmojiPayload(spritesheets=False)

        # GET
        response_get: Response = get_list_available_emoji(payload)
        assert response_get.status_code == 200
        response_get_dto: GetListAvailableEmojiDto = deserialize_and_validate_json(
            response_get, GetListAvailableEmojiDto
        )
        expected_response_get_dto: GetListAvailableEmojiDto = get_expected_response_dto(self.common_file_name)
        compare_objects(response_get_dto, expected_response_get_dto)

    def test_p4_should_get_list_available_emoji_with_other_locale_and_when_spritesheets_is_true(self) -> None:
        file_name: str = "P4_ExpectedGetListAvailableEmojiResponse.json"
        payload: GetListAvailableEmojiPayload = GetListAvailableEmojiPayload(
            locale="en-US",
            spritesheets=True,
        )

        # GET
        response_get: Response = get_list_available_emoji(payload)
        assert response_get.status_code == 200
        response_get_dto: GetListAvailableEmojiDto = deserialize_and_validate_json(
            response_get, GetListAvailableEmojiDto
        )
        expected_response_get_dto: GetListAvailableEmojiDto = get_expected_response_dto(file_name)
        compare_objects(response_get_dto, expected_response_get_dto)

    # ==========================================================================================================
    # NEGATIVE TESTS
    # ==========================================================================================================

    def test_n1_should_not_get_list_available_emoji_when_locale_has_incorrect_value(self) -> None:
        payload: GetListAvailableEmojiPayload = GetListAvailableEmojiPayload(locale="ABCDabcdĄŚąś1234!@#$")

        # GET
        response_get: Response = get_list_available_emoji(payload)
        assert response_get.status_code == 400
        assert response_get.text == "invalid value for locale"

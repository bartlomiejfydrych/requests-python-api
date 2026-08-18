from urllib.parse import urlparse

from pydantic import AnyUrl

from dto.boards.GET_get_board_dto import GET_GetBoardDto
from dto.boards.PUT_update_board_dto import PUT_UpdateBoardDto
from endpoints.boards.GET_get_board_endpoint import get_get_board
from utils.utils_compare import compare_objects
from utils.response.utils_response_deserializer import deserialize_and_validate_json, \
    deserialize_and_validate_json_with_business_rules


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -------------------------
# PREPARE EXPECTED RESPONSE
# -------------------------

def prepare_expected_response_put(
        expected_response: str,
        board_id: str,
        board_name: str,
        board_url: AnyUrl,
        board_short_url: AnyUrl,
) -> PUT_UpdateBoardDto:
    # Converting JSON String to DTO Object
    expected_response_put_dto: PUT_UpdateBoardDto = deserialize_and_validate_json(
        expected_response,
        PUT_UpdateBoardDto
    )

    # Value replacement
    expected_response_put_dto.id = board_id
    expected_response_put_dto.name = board_name
    expected_response_put_dto.url = board_url
    expected_response_put_dto.short_url = board_short_url  # NOTE FOR ME: shortUrl -> short_url (snake_case)

    return expected_response_put_dto


# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_put(response_put_dto: PUT_UpdateBoardDto) -> None:
    response_get = get_get_board(response_put_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GET_GetBoardDto = deserialize_and_validate_json_with_business_rules(
        response_get,
        GET_GetBoardDto
    )

    compare_objects(
        response_put_dto,
        response_get_dto,
        PUT_UpdateBoardDto.FIELD_ORGANIZATION
    )


# -------------------------
# STRIP BOARD NAME FROM URL
# -------------------------

def strip_board_name_from_url(url: str) -> str:
    parsed_url = urlparse(url)
    parts = parsed_url.path.split("/")

    if len(parts) >= 3:
        return f"{parsed_url.scheme}://{parsed_url.netloc}/b/{parts[2]}"

    return url

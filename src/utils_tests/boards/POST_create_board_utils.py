import time

from tests.base.test_base import TestBase
from dto.boards.POST_create_board_dto import POST_CreateBoardDto
from dto.boards.GET_get_board_dto import GET_GetBoardDto
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

def prepare_expected_response_post(
        expected_response: str,
        response_post_dto: POST_CreateBoardDto,
        board_name: str,
) -> POST_CreateBoardDto:
    # Converting JSON String to DTO Object
    expected_response_post_dto: POST_CreateBoardDto = deserialize_and_validate_json(expected_response,
                                                                                    POST_CreateBoardDto)
    # Value replacement
    expected_response_post_dto.id = response_post_dto.id
    expected_response_post_dto.name = board_name
    expected_response_post_dto.url = response_post_dto.url
    expected_response_post_dto.short_url = response_post_dto.short_url  # NOTE FOR ME: shortUrl -> short_url (snake_case)
    return expected_response_post_dto


# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_post(response_post_dto: POST_CreateBoardDto) -> None:
    response_get = get_get_board(response_post_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GET_GetBoardDto = deserialize_and_validate_json_with_business_rules(response_get, GET_GetBoardDto)
    compare_objects(response_post_dto, response_get_dto, POST_CreateBoardDto.FIELD_LIMITS)


# --------------------------
# GENERATE RANDOM BOARD NAME
# --------------------------

def generate_random_board_name() -> str:
    return f"{TestBase.faker.company()} borad {time.monotonic_ns()}"


# ---------------------------
# GENERATE RANDOM DESCRIPTION
# ---------------------------

def generate_random_desc() -> str:
    # NOTE FOR ME: python-faker nie ma 1:1 odpowiednika lorem().characters(min, max, upper, digits).
    # Poniżej pragmatyczny zamiennik generujący losowy tekst do 200 znaków.
    # Jeśli zależy Ci na czystych losowych znakach (nie słowach), użyj zamiast tego:
    #   import random, string
    #   return "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 200)))
    return TestBase.faker.text(max_nb_chars=200)

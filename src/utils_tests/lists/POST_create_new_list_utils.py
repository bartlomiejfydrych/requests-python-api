import time

from tests.base.test_base import TestBase
from dto.lists.GET_get_list_dto import GetListDto
from dto.lists.POST_create_new_list_dto import PostCreateNewListDto
from endpoints.lists.GET_get_list_endpoint import get_get_list
from utils.utils_compare import compare_objects
from utils.response.utils_response_deserializer import deserialize_and_validate_json_with_business_rules


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -------------------------
# GENERATE RANDOM LIST NAME
# -------------------------

def generate_random_list_name() -> str:
    return f"List - {TestBase.faker.company()} | Number: {time.monotonic_ns()}"


# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_post(response_post_dto: PostCreateNewListDto) -> None:
    response_get = get_get_list(response_post_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(
        response_get,
        GetListDto
    )

    compare_objects(
        response_post_dto,
        response_get_dto,
        PostCreateNewListDto.FIELD_LIMITS,
        PostCreateNewListDto.FIELD_SUBSCRIBED,
        PostCreateNewListDto.FIELD_SOFT_LIMIT
    )

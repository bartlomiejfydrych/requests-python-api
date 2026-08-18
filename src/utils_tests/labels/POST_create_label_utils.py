import time

from tests.base.test_base import TestBase
from dto.labels.GET_get_label_dto import GetLabelDto
from dto.labels.POST_create_label_dto import PostCreateLabelDto
from endpoints.labels.GET_get_label_endpoint import get_get_label
from utils.utils_compare import compare_objects
from utils.utils_random import pick_random
from utils.response.utils_response_deserializer import deserialize_and_validate_json_with_business_rules


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------------------------
# GENERATE RANDOM LABEL NAME
# --------------------------

def generate_random_label_name() -> str:
    return f"{TestBase.faker.company()} label {time.monotonic_ns()}"


# ---------------------------
# GENERATE RANDOM LABEL COLOR
# ---------------------------

def generate_random_label_color() -> str:
    return pick_random(
        "yellow",
        "purple",
        "blue",
        "red",
        "green",
        "orange",
        "black",
        "sky",
        "pink",
        "lime"
    )


# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_post(response_post_dto: PostCreateLabelDto) -> None:
    response_get = get_get_label(response_post_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GetLabelDto = deserialize_and_validate_json_with_business_rules(
        response_get,
        GetLabelDto
    )

    compare_objects(
        response_post_dto,
        response_get_dto,
        PostCreateLabelDto.FIELD_LIMITS
    )

from dto.labels.GET_get_label_dto import GetLabelDto
from dto.labels.PUT_update_label_dto import PutUpdateLabelDto
from endpoints.labels.GET_get_label_endpoint import get_get_label
from utils.response.utils_response_deserializer import deserialize_and_validate_json_with_business_rules
from utils.utils_compare import compare_objects


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_put(response_put_dto: PutUpdateLabelDto) -> None:
    response_get = get_get_label(response_put_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GetLabelDto = deserialize_and_validate_json_with_business_rules(
        response_get,
        GetLabelDto
    )

    compare_objects(
        response_put_dto,
        response_get_dto
    )

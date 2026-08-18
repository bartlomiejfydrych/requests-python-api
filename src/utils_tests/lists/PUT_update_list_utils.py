from dto.lists.GET_get_list_dto import GetListDto
from dto.lists.PUT_update_list_dto import PutUpdateListDto
from endpoints.lists.GET_get_list_endpoint import get_get_list
from utils.response.utils_response_deserializer import deserialize_and_validate_json_with_business_rules
from utils.utils_compare import compare_objects


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------------------------------------
# VALIDATE GET AGAINST PREVIOUS RESPONSE
# --------------------------------------

def validate_get_against_put(response_put_dto: PutUpdateListDto) -> None:
    response_get = get_get_list(response_put_dto.id)
    assert response_get.status_code == 200

    response_get_dto: GetListDto = deserialize_and_validate_json_with_business_rules(
        response_get,
        GetListDto
    )

    compare_objects(
        response_put_dto,
        response_get_dto,
        PutUpdateListDto.FIELD_SUBSCRIBED,
        GetListDto.FIELD_TYPE,
        GetListDto.FIELD_DATASOURCE
    )

from dto.emoji.GET_list_available_emoji_dto import GetListAvailableEmojiDto
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_file import read_expected_response_file_as_string

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

BASE_PATH = "emoji/GET_list_available_emoji/"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_expected_response_dto(file_name: str) -> GetListAvailableEmojiDto:
    json_string: str = read_expected_response_file_as_string(BASE_PATH + file_name)
    return deserialize_and_validate_json(json_string, GetListAvailableEmojiDto)

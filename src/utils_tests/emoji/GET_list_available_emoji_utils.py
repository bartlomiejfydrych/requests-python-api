from dto.emoji.GET_list_available_emoji_dto import GetListAvailableEmojiDto
from utils.utils_resources import read_json_file_as_object

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

BASE_PATH = "tests/expected_responses/emoji/GET_ListAvailableEmojiExpected/"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_expected_response_dto(file_name: str) -> GetListAvailableEmojiDto:
    return read_json_file_as_object(
        BASE_PATH + file_name,
        GetListAvailableEmojiDto
    )

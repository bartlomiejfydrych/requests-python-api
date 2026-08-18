from typing import Type, TypeVar

from dto.base_dto import BaseDto
from utils.response.utils_response_deserializer import deserialize_and_validate_json
from utils.utils_file import read_resource_file_as_string

T = TypeVar("T", bound=BaseDto)


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# EXAMPLE OF USE:
# board: BoardDto = read_json_file_as_object("payloads/boards/create_board_payload.json", BoardDto)

def read_json_file_as_object(resource_path: str, dto_class: Type[T]) -> T:
    json_string: str = read_resource_file_as_string(resource_path)
    return deserialize_and_validate_json(json_string, dto_class)

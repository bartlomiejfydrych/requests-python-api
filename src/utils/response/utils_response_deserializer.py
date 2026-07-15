from typing import Type, TypeVar, Union

from pydantic import TypeAdapter, ValidationError
from requests import Response

from dto.base_dto import BaseDto
from exceptions.exception_dto_deserialization import ExceptionDtoDeserialization
from utils.response.utils_response_json_parser import parse_string_to_json

T = TypeVar("T", bound=BaseDto)


# ==============================================================================================================
# METHODS - MAIN
# ==============================================================================================================

# ----------------------
# OBJECT DESERIALIZATION
# ----------------------

# EXAMPLE OF USE:
# user: UserDto = deserialize_and_validate_json(response, UserDto)

def deserialize_and_validate_json(source: Union[Response, str], dto_class: Type[T]) -> T:
    json_string: str = source.text if isinstance(source, Response) else source

    data = parse_string_to_json(json_string)

    try:
        return dto_class.model_validate(data)
    except ValidationError as e:
        raise ExceptionDtoDeserialization(
            f"Failed to deserialize and validate JSON into {dto_class.__name__}:\n{e}"
        ) from e


# --------------------
# LIST DESERIALIZATION
# --------------------

# EXAMPLE OF USE:
# users: list[UserDto] = deserialize_and_validate_json_list(response, UserDto)

def deserialize_and_validate_json_list(source: Union[Response, str], dto_class: Type[T]) -> list[T]:
    json_string: str = source.text if isinstance(source, Response) else source

    data = parse_string_to_json(json_string)

    if not isinstance(data, list):
        raise ExceptionDtoDeserialization(
            f"Expected a JSON array for list of {dto_class.__name__}, got {type(data).__name__}"
        )

    # noinspection PyTypeHints
    adapter: TypeAdapter = TypeAdapter(list[dto_class])

    try:
        return adapter.validate_python(data)
    except ValidationError as e:
        raise ExceptionDtoDeserialization(
            f"Failed to deserialize and validate JSON into list of {dto_class.__name__}:\n{e}"
        ) from e

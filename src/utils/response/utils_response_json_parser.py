import json
from typing import Any, Union

from requests import Response

from exceptions.exception_json_parsing import ExceptionJsonParsing


# ==============================================================================================================
# METHODS - MAIN
# ==============================================================================================================

def parse_string_to_json(json_string: str) -> Any:
    if json_string is None or json_string.strip() == "":
        raise ExceptionJsonParsing("JSON string is null or empty")

    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ExceptionJsonParsing("Failed to parse String into JSON") from e


# NOTE FOR ME:
# Do sytuacji, gdy nie chcę pełnego DTO - tylko wyciągnąć pojedyncze wartości
# z response, bez sprawdzania kompletności/zgodności struktury.
# Brakujące/nadmiarowe/zmienione nazwy pól nie mają tu żadnego znaczenia.
def parse_response_to_json(response: Response) -> Any:
    return parse_string_to_json(response.text)


"""
UŻYCIE W TEŚCIE:

response: Response = client.post(...)

data: dict = parse_response_to_json(response)

board_id: str = data["id"]
board_name: str = data.get("name")  # .get() zamiast [] gdy dopuszczasz brak klucza
"""

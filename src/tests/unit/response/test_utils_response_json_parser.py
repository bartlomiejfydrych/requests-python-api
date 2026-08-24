"""
NOTE FOR ME:
Funkcja UtilsResponseJsonParser.parseStringToJsonNode() w Javie zwraca obiekt Jackson JsonNode.
Python nie ma bezpośredniego odpowiednika – utils.response.utils_response_json_parser.parse_string_to_json() zwraca zwykły
dict/list/... (za pośrednictwem json.loads()), więc `node.get("name").asText()` staje się po prostu `result["name"]`.
"""

import pytest

from exceptions.exception_json_parsing import ExceptionJsonParsing
from utils.response.utils_response_json_parser import parse_string_to_json


@pytest.mark.unit
class TestUtilsResponseJsonParser:
    # ==========================================================================================================
    # TESTS
    # ==========================================================================================================

    def test_parse_string_to_json_when_none_should_raise_exception(self) -> None:
        with pytest.raises(ExceptionJsonParsing):
            # noinspection PyTypeChecker
            parse_string_to_json(None)

    def test_parse_string_to_json_when_blank_should_raise_exception(self) -> None:
        with pytest.raises(ExceptionJsonParsing):
            parse_string_to_json("   ")

    def test_parse_string_to_json_when_valid_json_should_return_dict(self) -> None:
        result = parse_string_to_json('{"name":"board"}')

        assert result["name"] == "board"

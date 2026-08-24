"""
NOTE FOR ME:
Test UtilsResponseDeserializerTest w Javie miał osobną klasę @Nested „ObjectTests” testującą gołą
deserializeJson() (tylko Jackson, bez walidacji Jakarta Bean) oraz osobną klasę @Nested „ValidationTests” testującą
deserializeAndValidateJson() (połączone walidacje Jackson i Jakarta). W Pythonie nie ma
odpowiednika dla „gołej deserializacji bez walidacji” — model_validate() w Pydantic zawsze wykonuje obie te czynności
jednocześnie — więc każdy przypadek przechodzi przez pojedynczą funkcję deserialize_and_validate_json().

Ważna różnica odkryta podczas przenoszenia: błędy wynikające z PARSOWANIA samego ciągu JSON (null, puste miejsce,
nieprawidłowa składnia) są zgłaszane jako ExceptionJsonParsing, pochodzące z parse_string_to_json() – funkcji wywoływanej
POZA blokiem try/except, który wychwytuje błąd ValidationError pydantic wewnątrz
_deserialize_and_validate_json_internal(). Tylko błędy wykryte PRZEZ Pydantic po pomyślnym sparsowaniu ciągu JSON
(nieznane pole, błędny typ, brakująca/nieprawidłowa wartość pola) są zawijane w
ExceptionDtoDeserialization. Dlatego niektóre przypadki ObjectTests w Javie są tutaj mapowane na ExceptionJsonParsing, a nie
ExceptionDtoDeserialization.

@Nested classes -> są przechowywane jako zagnieżdżone klasy testowe (pytest poprawnie zbiera zagnieżdżone klasy, odzwierciedlając strukturę Javy
"""

import pytest

from exceptions.exception_dto_deserialization import ExceptionDtoDeserialization
from exceptions.exception_json_parsing import ExceptionJsonParsing
from tests.unit.response.dto_fixtures import SampleDto, SampleParentDto, SampleValidatedDto
from utils.response.utils_response_deserializer import (
    deserialize_and_validate_json,
    deserialize_and_validate_json_list,
)


@pytest.mark.unit
class TestUtilsResponseDeserializer:
    # ==========================================================================================================
    # OBJECT DESERIALIZATION
    # ==========================================================================================================

    class TestObjectDeserialization:

        def test_deserialize_and_validate_json_when_valid_json_should_return_dto(self) -> None:
            json_string = '{"name":"test"}'

            dto = deserialize_and_validate_json(json_string, SampleDto)

            assert dto.name == "test"

        def test_deserialize_and_validate_json_when_invalid_json_should_raise_json_parsing_error(self) -> None:
            json_string = "{invalid json}"

            with pytest.raises(ExceptionJsonParsing):
                deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_json_contains_unknown_field_should_raise_exception(
                self) -> None:
            json_string = """
            {
                "name": "test",
                "unknown": "value"
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_wrong_type_should_raise_exception(self) -> None:
            json_string = """
            {
                "name": 123
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_empty_string_should_raise_json_parsing_error(self) -> None:
            json_string = ""

            with pytest.raises(ExceptionJsonParsing):
                deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_none_json_should_raise_json_parsing_error(self) -> None:
            with pytest.raises(ExceptionJsonParsing):
                # noinspection PyTypeChecker
                deserialize_and_validate_json(None, SampleDto)

    # ==========================================================================================================
    # VALIDATION
    # ==========================================================================================================

    class TestValidation:

        def test_deserialize_and_validate_json_when_dto_is_valid_should_pass(self) -> None:
            json_string = '{"name":"valid"}'

            deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_dto_is_invalid_should_raise_exception(self) -> None:
            json_string = '{"name":null}'

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleDto)

        def test_deserialize_and_validate_json_when_missing_field_should_raise_exception(self) -> None:
            json_string = "{}"

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleDto)

        # ----------
        # NESTED DTO
        # ----------

        def test_deserialize_and_validate_json_when_nested_valid_should_pass(self) -> None:
            json_string = """
            {
                "nested": {
                    "value": "ok"
                }
            }
            """

            deserialize_and_validate_json(json_string, SampleParentDto)

        def test_deserialize_and_validate_json_when_nested_field_missing_should_raise_exception(self) -> None:
            json_string = """
            {
                "nested": {}
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleParentDto)

        def test_deserialize_and_validate_json_when_nested_invalid_should_raise_exception(self) -> None:
            json_string = """
            {
                "nested": {
                    "value": null
                }
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleParentDto)

        # -----------------
        # FIELD CONSTRAINTS
        # -----------------

        def test_deserialize_and_validate_json_when_null_field_in_validated_dto_should_raise_exception(
                self) -> None:
            json_string = """
            {
                "name": null,
                "number": "123"
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleValidatedDto)

        def test_deserialize_and_validate_json_when_size_invalid_should_raise_exception(self) -> None:
            json_string = """
            {
                "name": "ab",
                "number": "123"
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleValidatedDto)

        def test_deserialize_and_validate_json_when_pattern_invalid_should_raise_exception(self) -> None:
            json_string = """
            {
                "name": "valid",
                "number": "abc"
            }
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json(json_string, SampleValidatedDto)

    # ==========================================================================================================
    # LISTS
    # ==========================================================================================================

    class TestLists:

        def test_deserialize_and_validate_json_list_when_list_valid_should_pass(self) -> None:
            json_string = """
            [
                {"name":"a"},
                {"name":"b"}
            ]
            """

            result = deserialize_and_validate_json_list(json_string, SampleDto)

            assert len(result) == 2

        def test_deserialize_and_validate_json_list_when_list_contains_invalid_dto_should_raise_exception(
                self) -> None:
            json_string = """
            [
                {"name":"ok"},
                {"name":null}
            ]
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json_list(json_string, SampleDto)

        def test_deserialize_and_validate_json_list_when_empty_list_should_pass(self) -> None:
            json_string = "[]"

            result = deserialize_and_validate_json_list(json_string, SampleDto)

            assert result == []

        def test_deserialize_and_validate_json_list_when_list_contains_null_should_raise_exception(
                self) -> None:
            json_string = """
            [
                {"name":"ok"},
                null
            ]
            """

            with pytest.raises(ExceptionDtoDeserialization):
                deserialize_and_validate_json_list(json_string, SampleDto)

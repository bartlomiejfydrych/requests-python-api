from dataclasses import dataclass

import pytest
from requests import Response

from utils.utils_compare import (
    SoftAssertions,
    compare_objects,
    compare_objects_soft,
    compare_response_with_json,
    compare_response_with_json_soft,
)


# ==========================================================================================================
# TEST DATA
# ==========================================================================================================

# NOTE FOR ME:
# CompareTestDto w Javie (zwykła klasa z getterami, zdefiniowana w osobnym pliku
# tests/unit/CompareTestDto.java) -> Klasa danych Pythona, przechowywana lokalnie w tym pliku, ponieważ zawiera tylko dane testowe.
# compare_objects()/compare_objects_soft() normalizuje klasy danych do słowników za pomocą _normalize_for_comparison(),
# i DeepDiff mogą również bezpośrednio przeszukiwać atrybuty zwykłych klas danych (używane poniżej do tworzenia ich list).
@dataclass
class CompareTestDto:
    name: str
    value: int


def _response_with_body(body: str) -> Response:
    response = Response()
    response.status_code = 200
    response._content = body.encode("utf-8")
    return response


@pytest.mark.unit
class TestUtilsCompare:
    # ==========================================================================================================
    # OBJECT COMPARISON – HARD
    # ==========================================================================================================

    def test_compare_objects_when_objects_are_equal_should_pass(self) -> None:
        actual = CompareTestDto("test", 10)
        expected = CompareTestDto("test", 10)

        compare_objects(actual, expected)

    def test_compare_objects_when_objects_differ_should_raise_assertion_error(self) -> None:
        actual = CompareTestDto("test", 10)
        expected = CompareTestDto("test", 99)

        with pytest.raises(AssertionError):
            compare_objects(actual, expected)

    def test_compare_objects_when_ignoring_field_should_pass(self) -> None:
        actual = CompareTestDto("test", 10)
        expected = CompareTestDto("test", 99)

        compare_objects(actual, expected, "value")

    # ==========================================================================================================
    # OBJECT COMPARISON – HARD (LISTS)
    # ==========================================================================================================

    def test_compare_objects_when_lists_are_equal_should_pass(self) -> None:
        actual = [CompareTestDto("A", 1), CompareTestDto("B", 2)]
        expected = [CompareTestDto("A", 1), CompareTestDto("B", 2)]

        compare_objects(actual, expected)

    def test_compare_objects_when_lists_differ_should_raise_assertion_error(self) -> None:
        actual = [CompareTestDto("A", 1), CompareTestDto("B", 2)]
        expected = [CompareTestDto("A", 1), CompareTestDto("B", 99)]

        with pytest.raises(AssertionError):
            compare_objects(actual, expected)

    def test_compare_objects_when_lists_differ_but_ignoring_field_should_pass(self) -> None:
        actual = [CompareTestDto("A", 1), CompareTestDto("B", 2)]
        expected = [CompareTestDto("A", 99), CompareTestDto("B", 88)]

        compare_objects(actual, expected, "value")

    # ==========================================================================================================
    # OBJECT COMPARISON – SOFT
    # ==========================================================================================================

    def test_compare_objects_soft_when_objects_are_equal_should_pass(self) -> None:
        actual = CompareTestDto("test", 10)
        expected = CompareTestDto("test", 10)

        with SoftAssertions() as softly:
            compare_objects_soft(softly, actual, expected)

    def test_compare_objects_soft_when_objects_differ_should_raise_assertion_error_on_assert_all(self) -> None:
        actual = CompareTestDto("test", 10)
        expected = CompareTestDto("test", 99)

        with pytest.raises(AssertionError):
            with SoftAssertions() as softly:
                compare_objects_soft(softly, actual, expected)

    # ==========================================================================================================
    # OBJECT COMPARISON – SOFT (LISTS)
    # ==========================================================================================================

    def test_compare_objects_soft_when_lists_are_equal_should_pass(self) -> None:
        actual = [CompareTestDto("A", 1), CompareTestDto("B", 2)]
        expected = [CompareTestDto("A", 1), CompareTestDto("B", 2)]

        with SoftAssertions() as softly:
            compare_objects_soft(softly, actual, expected)

    def test_compare_objects_soft_when_lists_differ_should_raise_assertion_error(self) -> None:
        actual = [CompareTestDto("A", 1), CompareTestDto("B", 2)]
        expected = [CompareTestDto("A", 1), CompareTestDto("B", 99)]

        with pytest.raises(AssertionError):
            with SoftAssertions() as softly:
                compare_objects_soft(softly, actual, expected)

    # ==========================================================================================================
    # JSON COMPARISON – OBJECT
    # ==========================================================================================================

    def test_compare_response_with_json_when_json_object_is_equal_should_pass(self) -> None:
        json_body = """
        {
          "name": "test",
          "value": 10
        }
        """

        response = _response_with_body(json_body)

        compare_response_with_json(response, json_body)

    def test_compare_response_with_json_when_json_object_differs_should_raise_assertion_error(self) -> None:
        actual_json = """
        {
          "name": "test",
          "value": 10
        }
        """
        expected_json = """
        {
          "name": "test",
          "value": 99
        }
        """

        response = _response_with_body(actual_json)

        with pytest.raises(AssertionError):
            compare_response_with_json(response, expected_json)

    def test_compare_response_with_json_when_ignoring_field_in_object_should_pass(self) -> None:
        actual_json = """
        {
          "name": "test",
          "value": 10
        }
        """
        expected_json = """
        {
          "name": "test",
          "value": 99
        }
        """

        response = _response_with_body(actual_json)

        compare_response_with_json(response, expected_json, "value")

    # ==========================================================================================================
    # JSON COMPARISON – ARRAY
    # ==========================================================================================================

    def test_compare_response_with_json_when_json_array_is_equal_should_pass(self) -> None:
        json_body = """
        [
          { "id": 1, "name": "A" },
          { "id": 2, "name": "B" }
        ]
        """

        response = _response_with_body(json_body)

        compare_response_with_json(response, json_body)

    def test_compare_response_with_json_when_json_array_differs_should_raise_assertion_error(self) -> None:
        actual_json = """
        [
          { "id": 1, "name": "A" },
          { "id": 2, "name": "B" }
        ]
        """
        expected_json = """
        [
          { "id": 1, "name": "A" },
          { "id": 99, "name": "B" }
        ]
        """

        response = _response_with_body(actual_json)

        with pytest.raises(AssertionError):
            compare_response_with_json(response, expected_json)

    def test_compare_response_with_json_when_ignoring_field_in_array_should_pass(self) -> None:
        actual_json = """
        [
          { "id": 1, "name": "A" },
          { "id": 2, "name": "B" }
        ]
        """
        expected_json = """
        [
          { "id": 99, "name": "A" },
          { "id": 88, "name": "B" }
        ]
        """

        response = _response_with_body(actual_json)

        compare_response_with_json(response, expected_json, "id")

    # ==========================================================================================================
    # JSON COMPARISON – NESTED
    # ==========================================================================================================

    def test_compare_response_with_json_when_ignoring_nested_field_should_pass(self) -> None:
        actual_json = """
        {
          "board": {
            "id": "123",
            "cards": [
              { "id": "a", "name": "Card A" },
              { "id": "b", "name": "Card B" }
            ]
          }
        }
        """
        expected_json = """
        {
          "board": {
            "id": "999",
            "cards": [
              { "id": "x", "name": "Card A" },
              { "id": "y", "name": "Card B" }
            ]
          }
        }
        """

        response = _response_with_body(actual_json)

        compare_response_with_json(response, expected_json, "id")

    # ==========================================================================================================
    # JSON COMPARISON – SOFT
    # ==========================================================================================================

    def test_compare_response_with_json_soft_when_json_differs_should_raise_assertion_error(self) -> None:
        actual_json = """
        {
          "name": "test",
          "value": 10
        }
        """
        expected_json = """
        {
          "name": "test",
          "value": 99
        }
        """

        response = _response_with_body(actual_json)

        with pytest.raises(AssertionError):
            with SoftAssertions() as softly:
                compare_response_with_json_soft(softly, response, expected_json)

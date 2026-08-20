"""
NOTES FOR ME:

Wymagana zależność:
    pip install deepdiff

WAŻNA RÓŻNICA względem oryginału z AssertJ:
    AssertJ's RecursiveComparisonConfiguration.ignoreFields(...) domyślnie
    dopasowuje pole po PEŁNEJ ścieżce od korzenia (np. "address.city"),
    a NIE po samej nazwie pola na każdej głębokości zagnieżdżenia.

    Poniższa implementacja (dla compare_objects/compare_objects_soft)
    ignoruje pole po NAZWIE, niezależnie od głębokości zagnieżdżenia -
    czyli tak jak oryginalna metoda removeFieldsRecursively() z Javy
    (która w oryginale była używana tylko do porównań JSON-a).
    W praktyce w testach API to zwykle wygodniejsze (np. "ignoruj id/createdAt
    wszędzie, gdzie się pojawią"), ale jeśli potrzebujesz dopasowania
    po dokładnej ścieżce - zobacz funkcję _build_exact_path_regex() na końcu.

WAŻNA RÓŻNICA w wersjach "soft":
    compare_objects_soft() i compare_response_with_json_soft() NIE tworzą już
    własnego, jednorazowego obiektu SoftAssertions i nie wołają assert_all()
    w środku. Przyjmują zewnętrzny obiekt SoftAssertions jako pierwszy
    argument, więc można nim "zbierać" wiele porównań w jednym teście
    i zgłosić wszystkie niezgodności na końcu, jednym wywołaniem
    softly.assert_all() - tak jak w prawdziwym AssertJ:

        softly = SoftAssertions()
        compare_objects_soft(softly, actual_user, expected_user, "id")
        compare_response_with_json_soft(softly, response, expected_json, "id")
        softly.assert_all()

    albo, wygodniej, jako context manager (assert_all() wywoła się
    automatycznie na wyjściu z bloku "with"):

        with SoftAssertions() as softly:
            compare_objects_soft(softly, actual_user, expected_user, "id")
            compare_response_with_json_soft(softly, response, expected_json, "id")
"""

import copy
import json
import re
from typing import Any, Callable, List, Tuple
from dataclasses import asdict, is_dataclass

from deepdiff import DeepDiff
from pydantic import BaseModel


# ==========================================================================================================
# OBJECT COMPARE
# ==========================================================================================================

# ------------
# MAIN METHODS
# ------------

def compare_objects(actual_object: Any, expected_object: Any, *fields_to_ignore: str) -> None:
    """
    NOTES FOR ME:
    Odpowiednik:
        assertThat(actualObject)
            .usingRecursiveComparison(configWithIgnoredFields(fieldsToIgnore))
            .isEqualTo(expectedObject);

    Działa dla: dict, list, dataclass, zwykłych obiektów Pythonowych (porównywanych przez atrybuty), modeli pydantic itd.
    """
    diff = _recursive_diff(actual_object, expected_object, fields_to_ignore)
    assert not diff, (
        f"Objects are different (ignored fields: {fields_to_ignore}):\n{diff.pretty()}"
    )


def compare_objects_soft(
        softly: "SoftAssertions", actual_object: Any, expected_object: Any, *fields_to_ignore: str
) -> None:
    """
    NOTES FOR ME:
    W przeciwieństwie do oryginalnego kodu Java (gdzie SoftAssertions był
    tworzony lokalnie i assertAll() wołane natychmiast), ta funkcja
    przyjmuje współdzielony obiekt `softly` i NIE woła assert_all().
    Dzięki temu można jej użyć wielokrotnie w jednym teście, a wszystkie
    niezgodności zostaną zgłoszone razem, dopiero gdy sam wywołasz
    softly.assert_all() (albo wyjdziesz z bloku "with SoftAssertions()").
    """
    diff = _recursive_diff(actual_object, expected_object, fields_to_ignore)
    softly.check(
        not diff,
        f"Objects are different (ignored fields: {fields_to_ignore}):\n{diff.pretty() if diff else ''}",
    )


# EXAMPLE OF USE:
# assert_satisfies_any_of(
#     actual_object,
#     lambda obj: compare_objects(obj, expected_variant_a),
#     lambda obj: compare_objects(obj, expected_variant_b),
# )

def assert_satisfies_any_of(actual_object: Any, *conditions: "Callable[[Any], None]") -> None:
    """
    NOTES FOR ME:
    Odpowiednik AssertJ's:
        assertThat(actualObject).satisfiesAnyOf(condition1, condition2, ...);

    Przechodzi, jeśli PRZYNAJMNIEJ JEDEN z warunków (funkcji przyjmujących `actual_object`
    i rzucających AssertionError w razie niezgodności - np. lambda z compare_objects w środku)
    zakończy się bez wyjątku. Jeśli WSZYSTKIE warunki zawiodą, zgłasza jeden AssertionError
    zbierający komunikaty ze wszystkich prób.
    """
    errors: list[str] = []

    for condition in conditions:
        try:
            condition(actual_object)
            return
        except AssertionError as e:
            errors.append(str(e))

    raise AssertionError(
        "None of the conditions were satisfied:\n" + "\n---\n".join(errors)
    )


# --------------
# HELPER METHODS
# --------------

def _build_field_name_regex(field: str) -> str:
    """
    NOTES FOR ME:
    Regex dopasowujący pole o danej nazwie niezależnie od głębokości
    zagnieżdżenia, działa zarówno dla ścieżek-atrybutów (root.field),
    jak i ścieżek-słownikowych (root['field']), które generuje DeepDiff.
    """
    escaped = re.escape(field)
    return rf"(\.{escaped}\b|\['{escaped}'\])"


def _build_exact_path_regex(path: str) -> str:
    """
    NOTES FOR ME:
    Dopasowanie po PEŁNEJ ścieżce od korzenia, np. "address.city".
    Nieużywana domyślnie.
    """
    parts = path.split(".")
    escaped_parts = [re.escape(p) for p in parts]
    dict_style = r"\['" + r"\']\['".join(escaped_parts) + r"\']"
    attr_style = r"\." + r"\.".join(escaped_parts) + r"\b"
    return rf"({attr_style}|{dict_style})$"


def _exclude_regex_paths(fields_to_ignore: Tuple[str, ...]) -> List[str]:
    return [_build_field_name_regex(f) for f in fields_to_ignore]


def _normalize_for_comparison(obj: Any) -> Any:
    """
    NOTES FOR ME:
    Normalizes objects before comparing them with DeepDiff.

    - Pydantic models -> dict (using JSON aliases, if defined)
    - dataclasses -> dict
    - other objects -> unchanged

    Thanks to this, two different DTO classes having the same structure
    (e.g. POST_CreateBoardDto vs GET_GetBoardDto) can still be compared
    recursively, similarly to AssertJ usingRecursiveComparison().
    """
    if isinstance(obj, BaseModel):
        return obj.model_dump(mode="python", by_alias=True)

    if is_dataclass(obj):
        return asdict(obj)

    return obj


def _recursive_diff(actual: Any, expected: Any, fields_to_ignore: Tuple[str, ...]) -> DeepDiff:
    return DeepDiff(
        _normalize_for_comparison(expected),
        _normalize_for_comparison(actual),
        exclude_regex_paths=_exclude_regex_paths(fields_to_ignore),
    )


# ==========================================================================================================
# JSON COMPARE
# ==========================================================================================================

# ------------
# MAIN METHODS
# ------------

def compare_response_with_json(response: Any, expected_response_json_string: str, *fields_to_ignore: str) -> None:
    """`response` is a requests.Response object."""
    actual = _strip_fields(response.json(), fields_to_ignore)
    expected = _strip_fields(json.loads(expected_response_json_string), fields_to_ignore)

    diff = DeepDiff(expected, actual)
    assert not diff, (
        f"JSON comparison failed (ignored fields: {fields_to_ignore}):\n{diff.pretty()}"
    )


def compare_response_with_json_soft(
        softly: "SoftAssertions", response: Any, expected_response_json_string: str, *fields_to_ignore: str
) -> None:
    """
    NOTES FOR ME:
    Tak jak compare_objects_soft() - przyjmuje współdzielony obiekt
    SoftAssertions i NIE woła assert_all() w środku, więc kilka takich
    porównań w jednym teście zgłosi się razem na końcu.
    """
    actual = _strip_fields(response.json(), fields_to_ignore)
    expected = _strip_fields(json.loads(expected_response_json_string), fields_to_ignore)

    diff = DeepDiff(expected, actual)

    softly.check(
        not diff,
        f"JSON comparison after ignoring fields [{', '.join(fields_to_ignore)}] failed:\n"
        f"{diff.pretty() if diff else ''}",
    )


# --------------
# HELPER METHODS
# --------------

def _remove_fields_recursively(node: Any, fields_to_ignore: Tuple[str, ...]) -> None:
    """
    Removes the given fields from a dict/list recursively (worked on ObjectNode/ArrayNode).
    Modifies the structure in place.
    """
    if node is None or not fields_to_ignore:
        return

    if isinstance(node, dict):
        for field in fields_to_ignore:
            node.pop(field, None)
        for value in node.values():
            _remove_fields_recursively(value, fields_to_ignore)

    elif isinstance(node, list):
        for item in node:
            _remove_fields_recursively(item, fields_to_ignore)


def _strip_fields(data: Any, fields_to_ignore: Tuple[str, ...]) -> Any:
    """Copies a structure and removes the fields to ignore from the copy (without mutating the original)."""
    data_copy = copy.deepcopy(data)
    _remove_fields_recursively(data_copy, fields_to_ignore)
    return data_copy


# ==========================================================================================================
# SOFT ASSERTIONS
# ==========================================================================================================

class SoftAssertions:
    """
    NOTES FOR ME:
    Pozwala wykonać wiele sprawdzeń (check) - w tym wiele wywołań
    compare_objects_soft()/compare_response_with_json_soft() - i zgłosić
    wszystkie niepowodzenia na koniec, jednym wywołaniem assert_all().

    Wariant 1 - jawne assert_all():

        softly = SoftAssertions()
        softly.check(actual.status == 200, "status powinien być 200")
        compare_objects_soft(softly, actual_user, expected_user, "id")
        softly.assert_all()

    Wariant 2 - jako context manager (assert_all() wywoła się
    automatycznie przy wyjściu z bloku "with", o ile w bloku nie wyleciał
    inny, niezwiązany wyjątek):

        with SoftAssertions() as softly:
            softly.check(actual.status == 200, "status powinien być 200")
            compare_objects_soft(softly, actual_user, expected_user, "id")
    """

    def __init__(self) -> None:
        self._errors: List[str] = []

    def check(self, condition: bool, message: str) -> None:
        if not condition:
            self._errors.append(message)

    def assert_all(self) -> None:
        if self._errors:
            details = "\n".join(f"- {err}" for err in self._errors)
            raise AssertionError(f"Soft assertion failures ({len(self._errors)}):\n{details}")

    def __enter__(self) -> "SoftAssertions":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        If another exception (e.g. a network error) is thrown in the "with" block,
        we do not mask it with an assert_all() call - we let it go.
        """
        if exc_type is None:
            self.assert_all()

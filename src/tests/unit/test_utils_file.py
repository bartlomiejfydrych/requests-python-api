"""
NOTE FOR ME:
Metoda UtilsFile.readResourceFileAsString() języka Java zgłasza wyjątek IllegalArgumentException("Zasób nie został znaleziony: ...")
gdy brakuje zasobu. Przeniesiona już metoda utils.utils_file.read_resource_file_as_string() języka Python
wywołuje wbudowany wyjątek FileNotFoundError z komunikatem "Plik nie został znaleziony: ..." — ten test sprawdza
RZECZYWISTE zachowanie implementacji języka Python, a nie dosłowne tłumaczenie typu komunikatu/wyjątku języka Java.

Poniżej użyty plik zasobu (sources/tests/unit/sample.txt, rozwiązany względem src/resources/) musi
znajdować się w repozytorium — musi mieć taką samą zawartość jak plik src/test/resources/tests/unit/sample.txt języka Java:
    Hello test file!
    Line 2
"""

import pytest

from utils.utils_file import read_resource_file_as_string


@pytest.mark.unit
class TestUtilsFile:
    # ==========================================================================================================
    # SUCCESS
    # ==========================================================================================================

    def test_read_resource_file_as_string_when_resource_exists_should_return_content(self) -> None:
        resource_path = "tests/unit/sample.txt"

        content = read_resource_file_as_string(resource_path)

        assert "Hello test file!" in content
        assert "Line 2" in content

    # ==========================================================================================================
    # ERRORS
    # ==========================================================================================================

    def test_read_resource_file_as_string_when_resource_does_not_exist_should_raise_file_not_found_error(
            self) -> None:
        resource_path = "not-existing-file.txt"

        with pytest.raises(FileNotFoundError) as exc_info:
            read_resource_file_as_string(resource_path)

        assert "File not found" in str(exc_info.value)
        assert resource_path in str(exc_info.value)

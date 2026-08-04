import shutil
from pathlib import Path

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

# NOTE FOR ME:
# Java trzyma wyniki w {target/allure-results} (katalog budowy Mavena). Python nie ma odpowiednika
# {target/} - katalog wynikowy Allure trzymamy więc bezpośrednio w rootcie repozytorium jako
# {allure-results/} (dokładnie tam, gdzie wskazuje {--alluredir} w {pytest.ini}).
# Ścieżka do pliku: src/utils/utils_allure.py -> parent (utils) -> parent (src) -> parent (root repo).
_PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

_ALLURE_RESULTS_DIR = _PROJECT_ROOT_DIR / "allure-results"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------------------------------------------
# Method for cleaning data from previous tests
# --------------------------------------------

def clean_allure_results_directory() -> None:
    # NOTE FOR ME:
    # Java robi to ręcznie: {Files.walk} + sortowanie malejące + usuwanie plik-po-pliku (żeby najpierw
    # skasować zawartość katalogów, a dopiero potem same katalogi). {shutil.rmtree} robi dokładnie to samo
    # (rekurencyjne usunięcie całego drzewa) w jednej linii - Pythonowe uproszczenie bez utraty intencji.
    try:
        if _ALLURE_RESULTS_DIR.exists():
            shutil.rmtree(_ALLURE_RESULTS_DIR)

        _ALLURE_RESULTS_DIR.mkdir(parents=True)

    except OSError as e:
        raise RuntimeError(
            f"Failed to clean Allure results directory: {_ALLURE_RESULTS_DIR}"
        ) from e

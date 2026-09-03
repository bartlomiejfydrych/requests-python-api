import shutil
from pathlib import Path

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

# NOTE FOR ME:
# Java trzyma wyniki w {target/allure-results} (katalog budowy Mavena). Python nie ma odpowiednika
# {target/} - katalog wynikowy Allure trzymamy więc bezpośrednio w rootcie repozytorium jako
# {allure-results/}.
# Ścieżka do pliku: src/utils/utils_allure.py -> parent (utils) -> parent (src) -> parent (root repo).
_PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# NOTE FOR ME:
# Brak podkreślnika (bez "_" na początku) celowo - to jedyne źródło prawdy dla lokalizacji tego
# katalogu. Root-owy {conftest.py} importuje tę stałą i wymusza ją jako {--alluredir} (nadpisując
# ewentualną wartość ustawioną przez IDE/wiersz poleceń), dzięki czemu katalog zawsze trafia w to samo
# miejsce niezależnie od {cwd}, z jakiego odpalane są testy (konsola / IDE / pojedyncza klasa).
ALLURE_RESULTS_DIR = _PROJECT_ROOT_DIR / "allure-results"


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
        if ALLURE_RESULTS_DIR.exists():
            shutil.rmtree(ALLURE_RESULTS_DIR)

        ALLURE_RESULTS_DIR.mkdir(parents=True)

    except OSError as e:
        raise RuntimeError(
            f"Failed to clean Allure results directory: {ALLURE_RESULTS_DIR}"
        ) from e

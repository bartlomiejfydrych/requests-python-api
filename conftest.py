from configuration.config import get_allure_report
from utils.utils_allure import ALLURE_RESULTS_DIR, clean_allure_results_directory


# NOTE FOR ME:
# {--alluredir=allure-results} w {pytest.ini} to ścieżka WZGLĘDNA - Allure tworzy ją względem {cwd}
# procesu, a nie względem katalogu, w którym leży {pytest.ini}/{conftest.py}. Z konsoli {cwd} to zwykle
# root repo, więc działa poprawnie - ale IDE potrafi ustawić {cwd} inaczej w zależności od sposobu
# odpalenia (cała sesja / pojedyncza klasa / pojedynczy plik), co skutkowało katalogiem {allure-results}
# tworzonym raz w rootcie, raz w {src/}, a raz nawet w {src/tests/unit}.
#
# {pytest_configure} to hook wołany przez pytest zaraz po sparsowaniu opcji (przed {pytest_sessionstart}
# i przed zebraniem testów), więc to najwcześniejszy moment, w którym można nadpisać opcję wtyczki
# {allure-pytest}. Nadpisujemy tu {config.option.allure_report_dir} (czyli to, co ustawia {--alluredir})
# na bezwzględną ścieżkę {ALLURE_RESULTS_DIR} - dokładnie tę samą, której używa
# {clean_allure_results_directory()} - dzięki czemu oba miejsca mają jedno wspólne źródło prawdy i
# katalog wynikowy zawsze trafia w to samo miejsce (root repo), niezależnie od {cwd} użytego przy
# odpaleniu testów.
def pytest_configure(config) -> None:
    config.option.allure_report_dir = str(ALLURE_RESULTS_DIR)


# NOTE FOR ME:
# Odpowiednik Javowego {GlobalTestExecutionListener} ({LauncherSessionListener.launcherSessionOpened()}).
# {pytest_sessionstart} to hook wołany przez pytest raz, na samym początku sesji testowej - zanim
# jakikolwiek test zostanie zebrany/uruchomiony - dokładnie tak jak {launcherSessionOpened} w JUnit
# Platform. Root-level {conftest.py} (a nie {conftest.py} w {src/tests/}) to jedyne miejsce, gdzie taki
# "globalny" hook ma sens - odpowiada temu, że {GlobalTestExecutionListener} jest rejestrowany raz dla
# całej sesji Mavena/Surefire, a nie per klasa testowa.
def pytest_sessionstart(session) -> None:
    if get_allure_report():
        clean_allure_results_directory()

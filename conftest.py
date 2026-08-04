from configuration.config import get_allure_report
from utils.utils_allure import clean_allure_results_directory


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

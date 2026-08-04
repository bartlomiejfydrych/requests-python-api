import allure
import requests

from configuration.config import get_logs_custom_color, get_logs_custom_optional, get_logs_mode
from enums.configuration.logs_mode import LogsMode
from loggers import allure_formatter, console_formatter, console_full_formatter


# NOTE FOR ME:
# Java-owy {HttpLogger} to klasa z konstruktorem, która raz zapamiętuje {mode}/{logOptional}/{colorEnabled}
# jako pola instancyjne (bo jedna instancja jest tworzona raz w {TestBase.configureLogging()}).
# Tutaj, zgodnie z konwencją "static class -> module-level functions" stosowaną w całym projekcie,
# nie ma żadnej instancji do trzymania - konfigurację czytamy bezpośrednio z {config.py} przy każdym
# wywołaniu {log()}. Koszt jest znikomy ({config.py} i tak cache'uje wczytanie {config.ini}), a zyskujemy
# brak dodatkowego stanu do zarządzania.


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def log(response: requests.Response) -> None:
    mode = get_logs_mode()

    if mode == LogsMode.CUSTOM:
        console_formatter.log_full(
            response,
            get_logs_custom_optional(),
            get_logs_custom_color(),
        )

    elif mode == LogsMode.SHORT:
        console_formatter.log_short(response)

    elif mode == LogsMode.FULL:
        console_full_formatter.log_full(response)

    elif mode == LogsMode.OFF:
        pass  # brak logów konsoli

    # ✅ ALLURE zawsze działa (niezależnie od LOGS_MODE)
    attachment = allure_formatter.format_attachment(response)
    allure.attach(
        attachment.content,
        name=attachment.title,
        attachment_type=allure.attachment_type.JSON,
        extension="json",
    )

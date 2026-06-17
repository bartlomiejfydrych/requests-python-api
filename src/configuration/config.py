import configparser
import os
from typing import Optional

from dotenv import load_dotenv

from enums.configuration.logs_mode import LogsMode

# ==========================================================================================================
# PATHS
# ==========================================================================================================

# NOTE FOR ME: Root katalogu projektu (3 poziomy wyżej niż ten plik: src/configuration/config.py -> root)
_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

_CONFIG_INI_PATH = os.path.join(_ROOT_DIR, "resources", "configuration", "config.ini")
_ENV_PATH = os.path.join(_ROOT_DIR, "environment", ".env")

# ==========================================================================================================
# VARIABLES
# ==========================================================================================================

_properties = configparser.ConfigParser()
_loaded = False

# NOTE FOR ME: Wczytanie .env od razu (brak pliku nie powoduje błędu tak jak {ignoreIfMissing} w Javie)
load_dotenv(dotenv_path=_ENV_PATH)


# ==========================================================================================================
# CUSTOM EXCEPTION (odpowiednik IllegalStateException z Javy)
# ==========================================================================================================

class IllegalStateError(Exception):
    pass


# ==========================================================================================================
# LOAD CONFIGURATION FILE (config.ini)
# ==========================================================================================================

# NOTE FOR ME:
# Mechanizm, który zapewni, że plik config.ini będzie wczytany tylko raz i później re-używany
# dla wszystkich funkcji, które pobierają informacje z tego pliku konfiguracyjnego.

def _load_properties() -> None:
    global _loaded
    if _loaded:  # Prevents multiple readings
        return
    _loaded = True

    if not os.path.isfile(_CONFIG_INI_PATH):
        raise IllegalStateError(f"(CONFIG) File {{config.ini}} not found at {_CONFIG_INI_PATH}.")

    try:
        _properties.read(_CONFIG_INI_PATH)
    except configparser.Error as e:
        raise RuntimeError("(CONFIG) Unable to load file {config.ini}") from e


# ==========================================================================================================
# PROPERTY READER
# ==========================================================================================================

# ------
# STRING
# ------

def _get_property(key: str, default_value: Optional[str], section: str = "config") -> str:
    _load_properties()

    # 1. {system} – Get system environment variables
    env_value = os.environ.get(key)
    if env_value is not None:
        return env_value.strip()

    # 2. {.env} – Get properties from file (python-dotenv ładuje też do os.environ,
    #    ale sprawdzamy jawnie na wypadek braku load_dotenv w innym kontekście)
    dotenv_value = os.getenv(key)
    if dotenv_value is not None:
        return dotenv_value.strip()

    # 3. {config.ini} – Get properties from file
    if _properties.has_option(section, key):
        return _properties.get(section, key).strip()

    # 4. {default} – Get default property (if was provided)
    if default_value is not None:
        print(f"[WARNING] (CONFIG) Using default value for missing configuration key '{key}': {default_value}")
        return default_value

    # 5. {missing} – Get error if property is missing
    raise IllegalStateError(
        f"(CONFIG) Missing required configuration key: '{key}'. "
        f"Checked {{system environment}}, {{.env}} and {{config.ini}}."
    )


# -------
# BOOLEAN
# -------

def _get_property_bool(key: str, default_value: bool, section: str = "config") -> bool:
    raw = _get_property(key, str(default_value), section).lower()

    if raw == "true":
        return True
    if raw == "false":
        return False

    raise IllegalStateError(f"(CONFIG) Invalid boolean value for key '{key}': {raw}. Allowed: true/false")


# -------
# INTEGER
# -------

def _get_property_int(key: str, default_value: int, section: str = "config") -> int:
    raw = _get_property(key, str(default_value), section)
    try:
        return int(raw)
    except ValueError:
        raise IllegalStateError(f"(CONFIG) Invalid integer value for key '{key}': {raw}")


# ----
# LONG
# ----

# W Pythonie nie ma rozróżnienia int/long – funkcja pozostawiona dla zgodności nazewniczej z Javą.

def _get_property_long(key: str, default_value: int, section: str = "config") -> int:
    return _get_property_int(key, default_value, section)


# ------
# DOUBLE
# ------

def _get_property_double(key: str, default_value: float, section: str = "config") -> float:
    raw = _get_property(key, str(default_value), section)
    try:
        return float(raw)
    except ValueError:
        raise IllegalStateError(f"(CONFIG) Invalid double value for key '{key}': {raw}")


# ==========================================================================================================
# PUBLIC CONFIG GETTERS
# ==========================================================================================================

# ----------
# config.ini
# ----------

# ALLURE REPORT

# Get report inclusion {Allure}
def get_allure_report() -> bool:
    return _get_property_bool("allureReport", True)


# BASE URL

# Get API base {URL}
def get_base_url() -> str:
    return _get_property("baseUrl", "https://api.trello.com/1")


# Get API base URL {Protocol}
def get_base_url_protocol() -> str:
    return _get_property("baseUrlProtocol", "https")


# Get API base URL {Subdomain}
def get_base_url_subdomain() -> str:
    return _get_property("baseUrlSubdomain", "api")


# Get API base URL {Domain}
def get_base_url_domain() -> str:
    return _get_property("baseUrlDomain", "trello")


# Get API base URL {TLD}
def get_base_url_tld() -> str:
    return _get_property("baseUrlTLD", "com")


# Get API base URL {Number}
def get_base_url_number() -> str:
    return _get_property("baseUrlNumber", "1")


# ----
# .env
# ----

# LOGS MANAGEMENT

# [LOGS MODE] Get Logs Mode
def get_logs_mode() -> LogsMode:
    value = _get_property("LOGS_MODE", "OFF")
    return LogsMode.from_value(value)


# [LOGS MODE] Validate Logs Mode
def validate_logs_config() -> None:
    logs_mode = get_logs_mode()

    if logs_mode != LogsMode.CUSTOM:
        if get_logs_custom_optional() or get_logs_custom_color():
            print("[WARNING] (CONFIG) LOGS_CUSTOM_* options are ignored when LOGS_MODE != CUSTOM")


# [CUSTOM] Get Logs {OPTIONAL}
def get_logs_custom_optional() -> bool:
    return _get_property_bool("LOGS_CUSTOM_OPTIONAL", False)


# [CUSTOM] Get Logs {COLOR}
def get_logs_custom_color() -> bool:
    return _get_property_bool("LOGS_CUSTOM_COLOR", False)


# TRELLO API KEY & TOKEN

# Get Trello {API key}
def get_trello_api_key() -> str:
    return _get_property("TRELLO_API_KEY", None)


# Get Trello {token}
def get_trello_token() -> str:
    return _get_property("TRELLO_TOKEN", None)


# OTHER VARIABLES

# Get {Trello ID}
def get_trello_id() -> str:
    return _get_property("TRELLO_ID", "67d9d5e34d7b900257deed0e")

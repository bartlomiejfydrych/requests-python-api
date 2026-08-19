from pathlib import Path

from exceptions.exception_resource_read import ExceptionResourceRead

# ==========================================================================================================
# PATHS
# ==========================================================================================================

# NOTE FOR ME: Katalog "src" (2 poziomy wyżej niż ten plik: src/utils/utils_file.py -> src)
_SRC_DIR = Path(__file__).resolve().parent.parent

_RESOURCES_DIR: Path = _SRC_DIR / "resources"
_EXPECTED_RESPONSES_DIR: Path = _SRC_DIR / "expected_responses"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# EXAMPLE OF USE:
# body: str = read_resource_file_as_string("payloads/create-board.json")

def read_resource_file_as_string(resource_path: str) -> str:
    return _read_file_as_string(_RESOURCES_DIR, resource_path)


# EXAMPLE OF USE:
# expected_response_json_file: str = read_expected_response_file_as_string(
#     "emoji/GET_list_available_emoji/P4_ExpectedGetListAvailableEmojiResponse.json"
# )

def read_expected_response_file_as_string(expected_response_path: str) -> str:
    return _read_file_as_string(_EXPECTED_RESPONSES_DIR, expected_response_path)


# ==========================================================================================================
# METHODS – PRIVATE
# ==========================================================================================================

def _read_file_as_string(base_dir: Path, relative_path: str) -> str:
    file_path: Path = base_dir / relative_path

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {relative_path}")

    try:
        return file_path.read_text(encoding="utf-8")
    except OSError as e:
        raise ExceptionResourceRead(f"Failed to read file: {relative_path}") from e

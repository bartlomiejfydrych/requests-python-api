from pathlib import Path

from exceptions.exception_resource_read import ExceptionResourceRead

# ==========================================================================================================
# PATHS
# ==========================================================================================================

# NOTE FOR ME: Katalog "src" (2 poziomy wyżej niż ten plik: src/utils/utils_file.py -> src)
_SRC_DIR = Path(__file__).resolve().parent.parent

_RESOURCES_DIR: Path = _SRC_DIR / "resources"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# EXAMPLE OF USE:
# expected_response_json_file: str = read_resource_file_as_string(
#     "tests/expected_responses/emoji/GET_ListAvailableEmojiExpected/P4_ExpectedGetListAvailableEmojiResponse.json"
# )

def read_resource_file_as_string(resource_path: str) -> str:
    file_path: Path = _RESOURCES_DIR / resource_path

    if not file_path.is_file():
        raise FileNotFoundError(f"Resource not found: {resource_path}")

    try:
        return file_path.read_text(encoding="utf-8")
    except OSError as e:
        raise ExceptionResourceRead(f"Failed to read resource: {resource_path}") from e


"""
########################################################################################################################
MY ADDITIONAL NOTES
########################################################################################################################

-----------------------------
BONUS – REQUESTS USE-CASE
-----------------------------

body: str = read_resource_file_as_string("payloads/create-user.json").replace(
    "${username}", faker.name().username()
)

response: Response = session.post("/users", data=body)
assert response.status_code == 201
"""

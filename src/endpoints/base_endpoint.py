from configuration.requests_session.base_request_spec import BaseRequestSpec
from configuration.requests_session.config_request_spec import (
    get_request_specification,
    get_request_specification_without_api_key,
    get_request_specification_without_token,
)


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_specification() -> BaseRequestSpec:
    return get_request_specification()


def get_specification_without_api_key() -> BaseRequestSpec:
    return get_request_specification_without_api_key()


def get_specification_without_token() -> BaseRequestSpec:
    return get_request_specification_without_token()

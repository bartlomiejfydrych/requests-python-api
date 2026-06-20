from configuration.base_url_builder import build_base_url
from configuration.config import get_trello_api_key, get_trello_token
from configuration.requests_session.base_request_spec import BaseRequestSpec


# ==========================================================================================================
# BUILDERS
# ==========================================================================================================

def _base_request_spec(default_params: dict) -> BaseRequestSpec:
    return BaseRequestSpec(
        base_url=build_base_url(),
        default_params=default_params,
    )


def get_request_specification() -> BaseRequestSpec:
    return _base_request_spec({
        "key": get_trello_api_key(),
        "token": get_trello_token(),
    })


def get_request_specification_without_api_key() -> BaseRequestSpec:
    return _base_request_spec({
        "token": get_trello_token(),
    })


def get_request_specification_without_token() -> BaseRequestSpec:
    return _base_request_spec({
        "key": get_trello_api_key(),
    })

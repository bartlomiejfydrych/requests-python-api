from typing import Iterator

from endpoints.emoji.GET_list_available_emoji_endpoint import list_available_emoji
from endpoints.emoji.emoji_base_endpoint import ENDPOINT_EMOJI
from endpoints.utils.named_endpoint import NamedEndpoint

# ==========================================================================================================
# CONSTANTS
# ==========================================================================================================

_ENDPOINT = ENDPOINT_EMOJI


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def all() -> Iterator[NamedEndpoint]:
    yield NamedEndpoint(f"GET {_ENDPOINT}", lambda spec: list_available_emoji(None, spec))

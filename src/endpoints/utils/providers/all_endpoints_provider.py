from itertools import chain
from typing import Iterator

from endpoints.utils.named_endpoint import NamedEndpoint
from endpoints.utils.providers import boards_endpoints_provider
from endpoints.utils.providers import emoji_endpoints_provider
from endpoints.utils.providers import labels_endpoints_provider
from endpoints.utils.providers import lists_endpoints_provider


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def all() -> Iterator[NamedEndpoint]:
    return chain(
        boards_endpoints_provider.all(),
        labels_endpoints_provider.all(),
        lists_endpoints_provider.all(),
        emoji_endpoints_provider.all(),
    )

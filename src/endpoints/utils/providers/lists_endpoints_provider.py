from typing import Iterator

from endpoints.lists.GET_get_list_endpoint import get_list
from endpoints.lists.POST_create_new_list_endpoint import create_new_list
from endpoints.lists.PUT_update_list_endpoint import update_list
from endpoints.lists.lists_base_endpoint import ENDPOINT_LISTS
from endpoints.utils.named_endpoint import NamedEndpoint

# ==========================================================================================================
# CONSTANTS
# ==========================================================================================================

_DUMMY_ID = "dummyId"
_ENDPOINT = ENDPOINT_LISTS


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def all() -> Iterator[NamedEndpoint]:
    yield NamedEndpoint(f"GET {_ENDPOINT}/{{id}}", lambda spec: get_list(_DUMMY_ID, spec))
    yield NamedEndpoint(f"POST {_ENDPOINT}", lambda spec: create_new_list(None, "listName", None, spec))
    yield NamedEndpoint(f"PUT {_ENDPOINT}/{{id}}", lambda spec: update_list(_DUMMY_ID, None, spec))

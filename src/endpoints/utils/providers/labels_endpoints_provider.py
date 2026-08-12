from typing import Iterator

from endpoints.labels.DEL_delete_label_endpoint import delete_label
from endpoints.labels.GET_get_label_endpoint import get_label
from endpoints.labels.POST_create_label_endpoint import create_label
from endpoints.labels.PUT_update_label_endpoint import update_label
from endpoints.labels.labels_base_endpoint import ENDPOINT_LABELS
from endpoints.utils.named_endpoint import NamedEndpoint
from enums.query_parameters.labels.label_base_query_parameters import LabelBaseQueryParameters

# ==========================================================================================================
# CONSTANTS
# ==========================================================================================================

_DUMMY_ID = "dummyId"
_ENDPOINT = ENDPOINT_LABELS


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def all() -> Iterator[NamedEndpoint]:
    yield NamedEndpoint(f"DELETE {_ENDPOINT}/{{id}}", lambda spec: delete_label(_DUMMY_ID, spec))
    yield NamedEndpoint(f"GET {_ENDPOINT}/{{id}}", lambda spec: get_label(_DUMMY_ID, spec))
    yield NamedEndpoint(
        f"POST {_ENDPOINT}",
        lambda spec: create_label(
            None,
            LabelBaseQueryParameters.NAME.key,
            LabelBaseQueryParameters.COLOR.key,
            spec,
        ),
    )
    yield NamedEndpoint(f"PUT {_ENDPOINT}/{{id}}", lambda spec: update_label(_DUMMY_ID, None, spec))

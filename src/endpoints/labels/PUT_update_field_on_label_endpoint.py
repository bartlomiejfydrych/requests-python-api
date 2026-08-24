from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.labels.labels_base_endpoint import label_by_id

from enums.query_parameters.labels.label_base_query_parameters import LabelBaseQueryParameters
from enums.query_parameters.labels.PUT_update_field_on_label_query_parameters import (
    PutUpdateFieldOnLabelQueryParameters,
)


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

# -----------
# CORE METHOD
# -----------

def _update_field_on_label(
        request_path: str,
        field_value: Optional[str],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {}

    if field_value is not None:
        query_params[PutUpdateFieldOnLabelQueryParameters.VALUE.value] = field_value

    return spec.put(
        request_path,
        params=query_params,
    )


# -----
# UTILS
# -----

def _label_field_by_id(
        label_id: str,
        label_field: LabelBaseQueryParameters,
) -> str:
    return f"{label_by_id(label_id)}/{label_field.value}"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------
# POSITIVE
# --------

def put_update_field_on_label(
        label_id: str,
        label_field: LabelBaseQueryParameters,
        field_value: str,
) -> Response:
    return _update_field_on_label(
        _label_field_by_id(label_id, label_field),
        field_value,
        get_specification(),
    )


# --------
# NEGATIVE
# --------

def put_update_field_on_label_custom_field(
        label_id: str,
        label_field: str,
        field_value: str,
) -> Response:
    return _update_field_on_label(
        f"{label_by_id(label_id)}/{label_field}",
        field_value,
        get_specification(),
    )


def put_update_field_on_label_without_field_value(
        label_id: str,
        label_field: LabelBaseQueryParameters,
) -> Response:
    return _update_field_on_label(
        _label_field_by_id(label_id, label_field),
        None,
        get_specification(),
    )


def put_update_field_on_label_without_label_field(
        label_id: str,
) -> Response:
    return _update_field_on_label(
        label_by_id(label_id),
        None,
        get_specification(),
    )

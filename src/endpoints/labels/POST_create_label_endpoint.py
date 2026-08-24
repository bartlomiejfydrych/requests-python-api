from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.labels.labels_base_endpoint import ENDPOINT_LABELS

from enums.query_parameters.labels.label_base_query_parameters import LabelBaseQueryParameters
from enums.query_parameters.labels.POST_create_label_query_parameters import PostCreateLabelQueryParameters
from enums.query_parameters_values.interfaces.query_param_value import QueryParamValue

from payloads.labels.POST_create_label_payload import PostCreateLabelPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# --------------------------
# WITH REQUIRED QUERY PARAMS
# --------------------------

def create_label(
        board_id: str,
        label_name: str,
        label_color: Optional[str],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {
        LabelBaseQueryParameters.ID_BOARD.value: board_id,
        LabelBaseQueryParameters.NAME.value: label_name,
        PostCreateLabelQueryParameters.COLOR.value: label_color,
    }

    return spec.post(
        ENDPOINT_LABELS,
        params=query_params,
    )


def post_create_label(
        board_id: str,
        label_name: str,
        label_color: Optional[str | QueryParamValue],
) -> Response:
    color_value = (
        label_color.value
        if label_color is not None and not isinstance(label_color, str)
        else label_color
    )

    return create_label(
        board_id,
        label_name,
        color_value,
        get_specification(),
    )


# ---------------
# WITH ANY PARAMS
# ---------------

def post_create_label_with_any_params(
        payload: Optional[PostCreateLabelPayload],
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return get_specification().post(
        ENDPOINT_LABELS,
        params=query_params,
    )

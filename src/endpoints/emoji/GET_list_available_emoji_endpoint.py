from typing import Optional

from requests import Response

from configuration.requests_session.base_request_spec import BaseRequestSpec
from endpoints.base_endpoint import get_specification
from endpoints.emoji.emoji_base_endpoint import ENDPOINT_EMOJI

from payloads.emoji.GET_list_available_emoji_payload import GetListAvailableEmojiPayload


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -----------------
# WITH QUERY PARAMS
# -----------------

def list_available_emoji(
        payload: Optional[GetListAvailableEmojiPayload],
        spec: BaseRequestSpec,
) -> Response:
    query_params = {}

    if payload is not None:
        query_params.update(payload.to_query_params())

    return spec.get(
        ENDPOINT_EMOJI,
        params=query_params,
    )


def get_list_available_emoji(
        payload: Optional[GetListAvailableEmojiPayload],
) -> Response:
    return list_available_emoji(payload, get_specification())

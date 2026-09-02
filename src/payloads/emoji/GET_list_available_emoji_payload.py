from dataclasses import dataclass
from typing import Optional

from payloads.base_payload import BasePayload
from enums.query_parameters.emoji.GET_list_available_emoji_query_parameters import \
    GetListAvailableEmojiQueryParameters as Get


@dataclass(kw_only=True)
class GetListAvailableEmojiPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    locale: Optional[str] = None
    spritesheets: Optional[bool] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Get.LOCALE, self.locale)
        self.put_if_not_null(params, Get.SPRITESHEETS, self.spritesheets)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = GetListAvailableEmojiPayload(
#     locale="Text",
#     spritesheets=True,
# )
#
# query_params = payload.to_query_params()

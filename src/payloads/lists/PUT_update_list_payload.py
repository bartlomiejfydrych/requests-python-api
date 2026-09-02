from dataclasses import dataclass
from typing import Optional

from payloads.base_payload import BasePayload
from enums.query_parameters.lists.lists.list_base_query_parameters import \
    ListBaseQueryParameters as Base
from enums.query_parameters.lists.lists.PUT_update_list_query_parameters import \
    PutUpdateListQueryParameters as Put


@dataclass(kw_only=True)
class PutUpdateListPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    name: Optional[str] = None
    closed: Optional[bool] = None
    id_board: Optional[str] = None
    pos: Optional[str | int] = None
    subscribed: Optional[bool] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Put.CLOSED, self.closed)
        self.put_if_not_null(params, Base.ID_BOARD, self.id_board)
        self.put_if_not_null(params, Base.POS, self.pos)
        self.put_if_not_null(params, Put.SUBSCRIBED, self.subscribed)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PutUpdateListPayload(
#     id_board="1",
#     name="Name",
#     closed=True,
#     pos="top",
#     subscribed=False,
# )
#
# query_params = payload.to_query_params()

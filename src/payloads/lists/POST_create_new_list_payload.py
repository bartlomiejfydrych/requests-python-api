from dataclasses import dataclass
from typing import Optional

from src.payloads.base_payload import BasePayload
from src.enums.query_parameters.lists.lists.list_base_query_parameters import \
    ListBaseQueryParameters as Base
from src.enums.query_parameters.lists.lists.POST_create_new_list_query_parameters import \
    PostCreateNewListQueryParameters as Post


@dataclass(kw_only=True)
class PostCreateNewListPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    name: Optional[str] = None
    id_board: Optional[str] = None
    id_list_source: Optional[str] = None
    pos: Optional[str | int] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Base.ID_BOARD, self.id_board)
        self.put_if_not_null(params, Post.ID_LIST_SOURCE, self.id_list_source)
        self.put_if_not_null(params, Post.POS, self.pos)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PostCreateNewListPayload(
#     id_board="1",
#     name="Name",
#     id_list_source="2",
#     pos="top",
# )
#
# query_params = payload.to_query_params()

from dataclasses import dataclass
from typing import Optional

from src.payloads.base_payload import BasePayload
from src.enums.query_parameters.labels.label_base_query_parameters import \
    LabelBaseQueryParameters as Base
from src.enums.query_parameters.labels.POST_create_label_query_parameters import \
    PostCreateLabelQueryParameters as Post


@dataclass(kw_only=True)
class PostCreateLabelPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    id_board: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Post.ID_BOARD, self.id_board)
        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Base.COLOR, self.color)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PostCreateLabelPayload(
#     id_board="1",
#     name="Name",
#     color="blue",
# )
#
# query_params = payload.to_query_params()

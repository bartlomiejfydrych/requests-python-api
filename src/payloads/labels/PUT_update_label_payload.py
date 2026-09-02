from dataclasses import dataclass
from typing import Optional

from payloads.base_payload import BasePayload
from enums.query_parameters.labels.label_base_query_parameters import \
    LabelBaseQueryParameters as Base


@dataclass(kw_only=True)
class PutUpdateLabelPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    name: Optional[str] = None
    color: Optional[str] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Base.COLOR, self.color)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PutUpdateLabelPayload(
#     name="Name",
#     color="blue",
# )
#
# query_params = payload.to_query_params()

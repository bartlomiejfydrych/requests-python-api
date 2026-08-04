from typing import ClassVar

from dto.lists.list_base_dto import ListBaseDto


class PutUpdateListDto(ListBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_SUBSCRIBED: ClassVar[str] = "subscribed"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    subscribed: bool | None

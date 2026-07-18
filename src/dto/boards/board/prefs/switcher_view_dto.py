from typing import ClassVar

from dto.base_dto import BaseDto


class SwitcherViewDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_VIEW_TYPE: ClassVar[str] = "viewType"
    FIELD_ENABLED: ClassVar[str] = "enabled"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    view_type: str
    enabled: bool

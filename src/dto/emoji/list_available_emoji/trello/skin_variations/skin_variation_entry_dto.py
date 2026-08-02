from typing import ClassVar

from dto.base_dto import BaseDto


class SkinVariationEntryDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_UNIFIED: ClassVar[str] = "unified"
    FIELD_NATIVE: ClassVar[str] = "native"
    FIELD_SHEET_X: ClassVar[str] = "sheetX"
    FIELD_SHEET_Y: ClassVar[str] = "sheetY"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    unified: str | None

    native_char: str | None

    sheet_x: int | None

    sheet_y: int | None

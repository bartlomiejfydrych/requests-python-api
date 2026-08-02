from typing import ClassVar

from dto.base_dto import BaseDto


class LabelBaseDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_ID: ClassVar[str] = "id"
    FIELD_ID_BOARD: ClassVar[str] = "idBoard"
    FIELD_NAME: ClassVar[str] = "name"
    FIELD_COLOR: ClassVar[str] = "color"
    FIELD_USES: ClassVar[str] = "uses"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    id: str

    id_board: str

    name: str

    color: str | None

    uses: int

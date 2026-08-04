from typing import ClassVar

from dto.base_dto import BaseDto


class ListBaseDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_ID: ClassVar[str] = "id"
    FIELD_NAME: ClassVar[str] = "name"
    FIELD_CLOSED: ClassVar[str] = "closed"
    FIELD_COLOR: ClassVar[str] = "color"
    FIELD_ID_BOARD: ClassVar[str] = "idBoard"
    FIELD_POS: ClassVar[str] = "pos"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    id: str

    name: str

    closed: bool

    color: str | None

    id_board: str

    pos: int

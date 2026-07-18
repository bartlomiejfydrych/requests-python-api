from typing import Any, ClassVar

from dto.boards.board_base_dto import BoardBaseDto


class POST_CreateBoardDto(BoardBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # FIELD_ID, FIELD_NAME, FIELD_DESC_DATA itd. są odziedziczone z BoardBaseDto -
    # tutaj dopisujemy tylko stałą dla nowego pola, którego nie ma w klasie bazowej.

    FIELD_LIMITS: ClassVar[str] = "limits"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Tak jak w idEnterprise z BoardBaseDto - brak @Valid w Javie (typ Object, nieokreślona
    # struktura) -> tu odpowiednik to Any. Gdy poznamy realny kształt tego pola, można
    # zamienić na dedykowany DTO.
    limits: Any

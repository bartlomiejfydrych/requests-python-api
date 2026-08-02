from typing import Any, ClassVar

from dto.labels.label_base_dto import LabelBaseDto


class PostCreateLabelDto(LabelBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_LIMITS: ClassVar[str] = "limits"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Pole pochodzi z Object w Javie.
    # Odpowiednikiem w Pythonie jest Any.
    #
    # Gdy poznamy realny kształt tego pola, można zamienić na dedykowany DTO.

    limits: Any

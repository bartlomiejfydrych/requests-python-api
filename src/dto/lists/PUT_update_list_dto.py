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

    # NOTE FOR ME:
    # Java: "subscribed" jest zwykłym polem @JsonProperty POZA konstruktorem @JsonCreator (bez
    # required=true) -> w pełni opcjonalne, Trello zwraca ten klucz tylko wtedy, gdy był częścią
    # payloadu PUT (np. przy zmianie tylko "pos"/"name"/"idBoard" klucz "subscribed" w ogóle nie
    # występuje w odpowiedzi).
    subscribed: bool | None = None

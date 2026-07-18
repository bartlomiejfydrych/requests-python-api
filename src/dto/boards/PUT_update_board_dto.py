from typing import ClassVar, Optional

from dto.boards.board_base_dto import BoardBaseDto
from dto.boards.board.organization_dto import OrganizationDto


class PUT_UpdateBoardDto(BoardBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_ORGANIZATION: ClassVar[str] = "organization"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Pole "organization":
    # - raz występuje w response, raz nie -> Optional[...] = None (nie NotNull)
    # - ma być walidowane TYLKO gdy się pojawi -> wystarczy typ OrganizationDto (dziedziczy
    #   po BaseDto), Pydantic waliduje automatycznie, ale TYLKO jeśli klucz jest obecny w JSON-ie
    # - brak pola w JSON-ie NIE powoduje błędu deserializacji -> zapewnia domyślna wartość None
    #
    # W Javie ten sam efekt osiągnięto przez WYJĘCIE pola z @JsonCreator (więc nie mogło mieć
    # required=true) i brak @NotNull. W Pydantic nie trzeba nic "wyjmować" z konstruktora -
    # jest jeden, spójny sposób zapisu: Optional[TYP] = None.
    organization: Optional[OrganizationDto] = None

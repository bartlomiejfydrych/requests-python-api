from typing import Any, ClassVar

from pydantic import AnyUrl, Field

from dto.base_dto import BaseDto
from dto.boards.board.desc_data_dto import DescDataDto
from dto.boards.board.prefs_dto import PrefsDto
from dto.boards.board.label_names_dto import LabelNamesDto


class BoardBaseDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # WAŻNE: ClassVar – inaczej Pydantic uznałby je za pola modelu (i wymagałby ich w JSON-ie)!
    #
    # Te stałe trzymają nazwy pól, TAK JAK WYSTĘPUJĄ W JSON-ie (camelCase) -
    # analogicznie jak w Javie – bo tam, gdzie ich używamy (np. w DeepDiff.exclude_paths),
    # operujemy na strukturze surowego JSON-a/response'a, a nie na atrybutach Python.

    FIELD_ID: ClassVar[str] = "id"
    FIELD_NAME: ClassVar[str] = "name"
    FIELD_DESC: ClassVar[str] = "desc"
    FIELD_DESC_DATA: ClassVar[str] = "descData"
    FIELD_CLOSED: ClassVar[str] = "closed"
    FIELD_ID_ORGANIZATION: ClassVar[str] = "idOrganization"
    FIELD_ID_ENTERPRISE: ClassVar[str] = "idEnterprise"
    FIELD_PINNED: ClassVar[str] = "pinned"
    FIELD_URL: ClassVar[str] = "url"
    FIELD_SHORT_URL: ClassVar[str] = "shortUrl"
    FIELD_PREFS: ClassVar[str] = "prefs"
    FIELD_LABEL_NAMES: ClassVar[str] = "labelNames"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Wszystkie nazwy pól - snake_case (PEP 8). Alias camelCase (np. "idOrganization")
    # generowany jest automatycznie przez alias_generator=to_camel z BaseDto – nie trzeba
    # go tu ręcznie dopisywać przez Field(alias=...).

    id: str = Field(pattern=r"^[0-9a-fA-F]{24}$")
    name: str = Field(min_length=1, max_length=16384)
    desc: str = Field(max_length=16384)

    # NOTE FOR ME:
    # Odpowiednik @Valid - wystarczy, że typ pola to klasa dziedzicząca po BaseDto.
    # Pydantic waliduje zagnieżdżone obiekty rekurencyjnie automatycznie, bez dodatkowej adnotacji.
    desc_data: DescDataDto | None

    closed: bool

    id_organization: str = Field(pattern=r"^[0-9a-fA-F]{24}$")

    # NOTE FOR ME:
    # W Javie brak @Valid, bo typ nieokreślony (Object) -> tu odpowiednik to Any.
    # Gdy poznamy realny kształt tego pola, można zamienić na dedykowany DTO.
    id_enterprise: Any

    pinned: bool

    url: AnyUrl
    short_url: AnyUrl

    prefs: PrefsDto
    label_names: LabelNamesDto

from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto
from dto.emoji.list_available_emoji.trello.skin_variations_dto import SkinVariationsDto


class TrelloDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_SKIN_VARIATIONS: ClassVar[str] = "skinVariations"
    FIELD_TTS: ClassVar[str] = "tts"
    FIELD_KEYWORDS: ClassVar[str] = "keywords"

    FIELD_UNIFIED: ClassVar[str] = "unified"
    FIELD_NAME: ClassVar[str] = "name"
    FIELD_NATIVE: ClassVar[str] = "native"
    FIELD_SHORT_NAME: ClassVar[str] = "shortName"
    FIELD_SHORT_NAMES: ClassVar[str] = "shortNames"
    FIELD_TEXT: ClassVar[str] = "text"
    FIELD_TEXTS: ClassVar[str] = "texts"
    FIELD_CATEGORY: ClassVar[str] = "category"
    FIELD_SHEET_X: ClassVar[str] = "sheetX"
    FIELD_SHEET_Y: ClassVar[str] = "sheetY"
    FIELD_SKIN_VARIATION: ClassVar[str] = "skinVariation"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    unified: str = Field(pattern=r"^[0-9A-Fa-f]{4,6}(?:-[0-9A-Fa-f]{4,6})*$")

    name: str

    # NOTE FOR ME:
    # UWAGA: "native" jest słowem kluczowym w Pythonie tylko jako część CPython API
    native_char: str

    short_name: str

    short_names: list[str]

    text: str | None

    texts: list[str] | None

    category: str

    sheet_x: int

    sheet_y: int

    skin_variation: str | None

    skin_variations: SkinVariationsDto | None

    tts: str | None

    keywords: list[str] | None

from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto
from dto.emoji.list_available_emoji.sprite_sheets.twitter.sprite_sheet_entry_dto import (
    SpriteSheetEntryDto,
)


class TwitterDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_16: ClassVar[str] = "16"
    FIELD_20: ClassVar[str] = "20"
    FIELD_32: ClassVar[str] = "32"
    FIELD_64: ClassVar[str] = "64"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Pole JSON zaczyna się od cyfry, więc nie może być nazwą atrybutu w Pythonie.
    # W tym przypadku alias trzeba ustawić ręcznie przez Field(alias=...),
    # ponieważ alias_generator nie jest w stanie wygenerować poprawnej nazwy.

    size_16: SpriteSheetEntryDto = Field(alias=FIELD_16)

    size_20: SpriteSheetEntryDto = Field(alias=FIELD_20)

    size_32: SpriteSheetEntryDto = Field(alias=FIELD_32)

    size_64: SpriteSheetEntryDto = Field(alias=FIELD_64)

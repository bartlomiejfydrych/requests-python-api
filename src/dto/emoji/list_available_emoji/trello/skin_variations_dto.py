from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto
from dto.emoji.list_available_emoji.trello.skin_variations.skin_variation_entry_dto import (
    SkinVariationEntryDto,
)


class SkinVariationsDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_1F3FB: ClassVar[str] = "1F3FB"
    FIELD_1F3FC: ClassVar[str] = "1F3FC"
    FIELD_1F3FD: ClassVar[str] = "1F3FD"
    FIELD_1F3FE: ClassVar[str] = "1F3FE"
    FIELD_1F3FF: ClassVar[str] = "1F3FF"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Pole JSON zaczyna się od cyfry, więc nie może być nazwą atrybutu w Pythonie.
    # W tym przypadku alias trzeba ustawić ręcznie przez Field(alias=...),
    # ponieważ alias_generator nie jest w stanie wygenerować poprawnej nazwy.

    one_f3fb: SkinVariationEntryDto | None = Field(alias=FIELD_1F3FB)
    one_f3fc: SkinVariationEntryDto | None = Field(alias=FIELD_1F3FC)
    one_f3fd: SkinVariationEntryDto | None = Field(alias=FIELD_1F3FD)
    one_f3fe: SkinVariationEntryDto | None = Field(alias=FIELD_1F3FE)
    one_f3ff: SkinVariationEntryDto | None = Field(alias=FIELD_1F3FF)

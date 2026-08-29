from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto


class SkinVariationEntryDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_UNIFIED: ClassVar[str] = "unified"
    FIELD_NATIVE: ClassVar[str] = "native"
    FIELD_SHEET_X: ClassVar[str] = "sheetX"
    FIELD_SHEET_Y: ClassVar[str] = "sheetY"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Java (SkinVariationEntry.java) - żadne pole nie ma @NotNull ani nie jest częścią @JsonCreator, więc
    # wszystkie są w pełni opcjonalne (klucz może w ogóle nie wystąpić) -> jawne "= None" dla każdego pola.
    unified: str | None = None

    # Klucz JSON to "native" (nie "nativeChar") - alias trzeba nadpisać ręcznie, tak jak w TrelloDto.
    native_char: str | None = Field(default=None, alias=FIELD_NATIVE)

    sheet_x: int | None = None

    sheet_y: int | None = None

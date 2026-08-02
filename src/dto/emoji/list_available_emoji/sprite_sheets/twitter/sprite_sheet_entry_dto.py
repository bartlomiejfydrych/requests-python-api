from typing import ClassVar

from pydantic import AnyUrl

from dto.base_dto import BaseDto


class SpriteSheetEntryDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_URL: ClassVar[str] = "url"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Java:
    #     @NotNull
    #     public URL url;
    #
    # Python:
    #     AnyUrl
    #
    # Pydantic automatycznie waliduje poprawność formatu URL.

    url: AnyUrl

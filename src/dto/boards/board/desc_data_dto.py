from typing import ClassVar

from dto.base_dto import BaseDto
from dto.boards.board.desc_data.emoji_dto import EmojiDto


class DescDataDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_EMOJI: ClassVar[str] = "emoji"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # Odpowiednik @Valid @NotNull - wystarczy sam typ EmojiDto (dziedziczy po BaseDto),
    # Pydantic waliduje zagnieżdżony obiekt automatycznie (odpowiednik @Valid),
    # a brak Optional wymusza, że pole jest wymagane i nie może być None (odpowiednik @NotNull).
    emoji: EmojiDto

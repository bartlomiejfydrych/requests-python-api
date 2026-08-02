from typing import ClassVar

from dto.base_dto import BaseDto
from dto.emoji.list_available_emoji.sprite_sheets_dto import SpriteSheetsDto
from dto.emoji.list_available_emoji.trello_dto import TrelloDto


class GetListAvailableEmojiDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_SPRITE_SHEETS: ClassVar[str] = "spriteSheets"
    FIELD_TRELLO: ClassVar[str] = "trello"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    sprite_sheets: SpriteSheetsDto | None
    trello: list[TrelloDto]

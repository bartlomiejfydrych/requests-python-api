from typing import ClassVar

from dto.base_dto import BaseDto
from dto.emoji.list_available_emoji.sprite_sheets.twitter_dto import TwitterDto


class SpriteSheetsDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_TWITTER: ClassVar[str] = "twitter"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    twitter: TwitterDto

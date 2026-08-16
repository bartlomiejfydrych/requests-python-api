from typing import Optional

from dto.labels.PUT_update_label_dto import PutUpdateLabelDto
from enums.query_parameters_values.labels.common.color import Color


class PutUpdateLabelExpected:

    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    def __init__(
            self,
            id: str = "DEFAULT_ID",
            id_board: str = "DEFAULT_BOARD_ID",
            name: str = "DEFAULT_NAME",
            color: Optional[str] = None,
            uses: int = 0
    ) -> None:
        self.id = id
        self.id_board = id_board
        self.name = name
        self.color = color
        self.uses = uses

    # ==========================================================================================================
    # CONSTRUCTORS
    # ==========================================================================================================

    # ----
    # BASE
    # ----

    @staticmethod
    def base() -> "PutUpdateLabelExpected":
        return PutUpdateLabelExpected()

    # ==========================================================================================================
    # METHODS (replacing data)
    # ==========================================================================================================

    def with_id(self, id: str) -> "PutUpdateLabelExpected":
        self.id = id
        return self

    def with_board_id(self, id_board: str) -> "PutUpdateLabelExpected":
        self.id_board = id_board
        return self

    def with_name(self, name: str) -> "PutUpdateLabelExpected":
        self.name = name
        return self

    # COLOR – START

    def with_color(self, color: Optional[str | Color]) -> "PutUpdateLabelExpected":
        if isinstance(color, Color):
            self.color = color.value
        else:
            self.color = color

        return self

    # COLOR – END

    def with_uses(self, uses: int) -> "PutUpdateLabelExpected":
        self.uses = uses
        return self

    # ==========================================================================================================
    # BUILDER
    # ==========================================================================================================

    def build(self) -> PutUpdateLabelDto:
        return PutUpdateLabelDto(
            id=self.id,
            id_board=self.id_board,
            name=self.name,
            color=self.color,
            uses=self.uses
        )


# ==========================================================================================================
# NEGATIVE TESTS (expected responses)
# ==========================================================================================================

# -----
# color
# -----

EXPECTED_PUT_LABEL_RESPONSE_INVALID_COLOR: str = """
{
    "message": "invalid value for color",
    "error": "ERROR"
}
"""

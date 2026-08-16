from typing import Any, Optional

from dto.labels.POST_create_label_dto import PostCreateLabelDto
from enums.query_parameters_values.labels.common.color import Color


class PostCreateLabelExpected:

    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    def __init__(
            self,
            id: str = "DEFAULT_ID",
            id_board: str = "DEFAULT_BOARD_ID",
            name: str = "DEFAULT_NAME",
            color: Optional[str] = None,
            uses: int = 0,
            limits: Optional[dict[str, Any]] = None
    ) -> None:
        self.id = id
        self.id_board = id_board
        self.name = name
        self.color = color
        self.uses = uses
        self.limits = limits if limits is not None else {}

    # ==========================================================================================================
    # CONSTRUCTORS
    # ==========================================================================================================

    # ----
    # BASE
    # ----

    @staticmethod
    def base() -> "PostCreateLabelExpected":
        return PostCreateLabelExpected()

    # ==========================================================================================================
    # METHODS (replacing data)
    # ==========================================================================================================

    def with_id(self, id: str) -> "PostCreateLabelExpected":
        self.id = id
        return self

    def with_board_id(self, id_board: str) -> "PostCreateLabelExpected":
        self.id_board = id_board
        return self

    def with_name(self, name: str) -> "PostCreateLabelExpected":
        self.name = name
        return self

    # COLOR – START

    def with_color(self, color: Optional[str | Color]) -> "PostCreateLabelExpected":
        if isinstance(color, Color):
            self.color = color.value
        else:
            self.color = color

        return self

    # COLOR – END

    def with_uses(self, uses: int) -> "PostCreateLabelExpected":
        self.uses = uses
        return self

    # Rather for the future, when limits will no longer be empty
    def with_limits(self, limits: dict[str, Any]) -> "PostCreateLabelExpected":
        self.limits = limits
        return self

    # ==========================================================================================================
    # BUILDER
    # ==========================================================================================================

    def build(self) -> PostCreateLabelDto:
        return PostCreateLabelDto(
            id=self.id,
            id_board=self.id_board,
            name=self.name,
            color=self.color,
            uses=self.uses,
            limits=self.limits
        )

    # ==========================================================================================================
    # EXAMPLE OF USE
    # ==========================================================================================================

    '''
    expected = (
        PostCreateLabelExpected
        .base()
        .with_id(response_json["id"])
        .with_board_id(board_id)
        .with_name(label_name)
        .with_color(Color.BLUE)
        .build()
    )
    '''


# ==========================================================================================================
# NEGATIVE TESTS (expected responses)
# ==========================================================================================================

# -------
# idBoard
# -------

EXPECTED_POST_LABEL_RESPONSE_INVALID_ID: str = """
{
    "message": "Invalid id",
    "error": "ERROR"
}
"""

# -----
# color
# -----

EXPECTED_POST_LABEL_RESPONSE_INVALID_COLOR: str = """
{
    "message": "invalid value for color",
    "error": "ERROR"
}
"""

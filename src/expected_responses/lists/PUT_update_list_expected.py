from typing import Optional

from dto.lists.PUT_update_list_dto import PutUpdateListDto


class PutUpdateListExpected:

    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # --------
    # REQUIRED
    # --------

    def __init__(
            self,
            id: str = "DEFAULT_ID",
            name: str = "DEFAULT_NAME",
            closed: bool = False,
            color: Optional[str] = None,
            id_board: str = "DEFAULT_BOARD_ID",
            pos: int = 1,
            subscribed: Optional[bool] = None
    ) -> None:
        self.id = id
        self.name = name
        self.closed = closed
        self.color = color
        self.id_board = id_board
        self.pos = pos

        # --------
        # OPTIONAL
        # --------

        self.subscribed = subscribed

    # ==========================================================================================================
    # CONSTRUCTORS
    # ==========================================================================================================

    # ----
    # BASE
    # ----

    @staticmethod
    def base() -> "PutUpdateListExpected":
        return PutUpdateListExpected()

    # ==========================================================================================================
    # METHODS (replacing data)
    # ==========================================================================================================

    def with_id(self, id: str) -> "PutUpdateListExpected":
        self.id = id
        return self

    def with_name(self, name: str) -> "PutUpdateListExpected":
        self.name = name
        return self

    def with_closed(self, closed: bool) -> "PutUpdateListExpected":
        self.closed = closed
        return self

    def with_color(self, color: Optional[str]) -> "PutUpdateListExpected":
        self.color = color
        return self

    def with_board_id(self, id_board: str) -> "PutUpdateListExpected":
        self.id_board = id_board
        return self

    def with_pos(self, pos: int) -> "PutUpdateListExpected":
        self.pos = pos
        return self

    def with_subscribed(self, subscribed: Optional[bool]) -> "PutUpdateListExpected":
        self.subscribed = subscribed
        return self

    # ==========================================================================================================
    # BUILDER
    # ==========================================================================================================

    def build(self) -> PutUpdateListDto:
        dto = PutUpdateListDto(
            id=self.id,
            name=self.name,
            closed=self.closed,
            color=self.color,
            id_board=self.id_board,
            pos=self.pos
        )

        # IMPORTANT: subscribed is optional in response
        if self.subscribed is not None:
            dto.subscribed = self.subscribed

        return dto


# ==========================================================================================================
# NEGATIVE TESTS (expected responses)
# ==========================================================================================================

# --
# id
# --

EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_ID: str = "invalid id"

# ----
# name
# ----

EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_NAME: str = """
{
  "message": "invalid value for name",
  "error": "BAD_REQUEST_ERROR"
}
"""

# -------
# idBoard
# -------

EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_BOARD_ID: str = """
{
    "message": "invalid id",
    "error": "BAD_REQUEST_ERROR"
}
"""

EXPECTED_PUT_UPDATE_LIST_RESPONSE_BOARD_NOT_FOUND: str = """
{
    "message": "Board not found.",
    "error": "BOARD_NOT_FOUND"
}
"""

# ---
# pos
# ---

EXPECTED_PUT_UPDATE_LIST_RESPONSE_INVALID_POSITION: str = """
{
    "message": "Invalid position.",
    "error": "ERROR"
}
"""

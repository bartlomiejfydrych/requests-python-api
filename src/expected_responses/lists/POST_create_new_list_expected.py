from typing import Any, Optional

from dto.lists.POST_create_new_list_dto import PostCreateNewListDto
from dto.lists.list.data_source_dto import DataSourceDto


class PostCreateNewListExpected:

    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    def __init__(
            self,
            id: str = "DEFAULT_ID",
            name: str = "DEFAULT_NAME",
            closed: bool = False,
            color: Optional[str] = None,
            id_board: str = "DEFAULT_BOARD_ID",
            pos: int = 1,
            type: Optional[str] = None,
            datasource: Optional[DataSourceDto] = None,
            limits: Optional[dict[str, Any]] = None,
            subscribed: bool = False,
            soft_limit: Optional[str] = None
    ) -> None:
        self.id = id
        self.name = name
        self.closed = closed
        self.color = color
        self.id_board = id_board
        self.pos = pos
        self.type = type
        self.datasource = datasource if datasource is not None else DataSourceDto(filter=False)
        self.limits = limits if limits is not None else {}
        self.subscribed = subscribed
        self.soft_limit = soft_limit

    # ==========================================================================================================
    # CONSTRUCTORS
    # ==========================================================================================================

    # ----
    # BASE
    # ----

    @staticmethod
    def base() -> "PostCreateNewListExpected":
        return PostCreateNewListExpected()

    # ==========================================================================================================
    # METHODS (replacing data)
    # ==========================================================================================================

    def with_id(self, id: str) -> "PostCreateNewListExpected":
        self.id = id
        return self

    def with_name(self, name: str) -> "PostCreateNewListExpected":
        self.name = name
        return self

    def with_board_id(self, id_board: str) -> "PostCreateNewListExpected":
        self.id_board = id_board
        return self

    def with_pos(self, pos: int) -> "PostCreateNewListExpected":
        self.pos = pos
        return self

    # ==========================================================================================================
    # BUILDER
    # ==========================================================================================================

    def build(self) -> PostCreateNewListDto:
        return PostCreateNewListDto(
            id=self.id,
            name=self.name,
            closed=self.closed,
            color=self.color,
            id_board=self.id_board,
            pos=self.pos,
            type=self.type,
            datasource=self.datasource,
            limits=self.limits,
            subscribed=self.subscribed,
            soft_limit=self.soft_limit
        )


# ==========================================================================================================
# NEGATIVE TESTS (expected responses)
# ==========================================================================================================

# ----
# name
# ----

EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_NAME: str = """
{
  "message": "invalid value for name",
  "error": "BAD_REQUEST_ERROR"
}
"""

# -------
# idBoard
# -------

EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_BOARD: str = "invalid value for idBoard"

# ------------
# idListSource
# ------------

EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_ID_LIST_SOURCE: str = """
{
    "message": "Invalid objectId",
    "error": "ERROR"
}
"""

# ---
# pos
# ---

EXPECTED_POST_NEW_LIST_RESPONSE_INVALID_POS: str = """
{
    "message": "Invalid position.",
    "error": "ERROR"
}
"""

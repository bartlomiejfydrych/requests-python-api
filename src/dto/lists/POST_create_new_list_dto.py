from typing import Any, ClassVar

from dto.lists.list.data_source_dto import DataSourceDto
from dto.lists.list_base_dto import ListBaseDto


class PostCreateNewListDto(ListBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_TYPE: ClassVar[str] = "type"
    FIELD_DATASOURCE: ClassVar[str] = "datasource"
    FIELD_LIMITS: ClassVar[str] = "limits"
    FIELD_SUBSCRIBED: ClassVar[str] = "subscribed"
    FIELD_SOFT_LIMIT: ClassVar[str] = "softLimit"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    type: str | None

    datasource: DataSourceDto

    limits: Any

    subscribed: bool | None

    soft_limit: str | None

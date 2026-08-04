from typing import ClassVar

from dto.lists.list.data_source_dto import DataSourceDto
from dto.lists.list_base_dto import ListBaseDto


class GetListDto(ListBaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_TYPE: ClassVar[str] = "type"
    FIELD_DATASOURCE: ClassVar[str] = "datasource"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    type: str | None

    datasource: DataSourceDto

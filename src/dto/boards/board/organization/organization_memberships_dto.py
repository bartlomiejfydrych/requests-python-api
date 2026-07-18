from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto


class OrganizationMembershipsDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_ID: ClassVar[str] = "id"
    FIELD_ID_MEMBER: ClassVar[str] = "idMember"
    FIELD_MEMBER_TYPE: ClassVar[str] = "memberType"
    FIELD_UNCONFIRMED: ClassVar[str] = "unconfirmed"
    FIELD_DEACTIVATED: ClassVar[str] = "deactivated"
    FIELD_LAST_ACTIVE: ClassVar[str] = "lastActive"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    id: str
    id_member: str
    member_type: str
    unconfirmed: bool
    deactivated: bool

    # NOTE FOR ME:
    # @Pattern z Javy używał podwójnego escapowania (\\d), bo string w Javie sam w sobie
    # wymaga escapowania backslasha. W Pythonie wystarczy raw string (prefiks r"...") -
    # \d nie trzeba podwójnie escapować, bo raw string przekazuje backslash dosłownie do regexu.
    last_active: str = Field(
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$"
    )

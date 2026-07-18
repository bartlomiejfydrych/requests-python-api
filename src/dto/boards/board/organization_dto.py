from typing import ClassVar

from pydantic import Field

from dto.base_dto import BaseDto
from dto.boards.board.organization.organization_memberships_dto import OrganizationMembershipsDto


class OrganizationDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_ID: ClassVar[str] = "id"
    FIELD_NAME: ClassVar[str] = "name"
    FIELD_DISPLAY_NAME: ClassVar[str] = "displayName"
    FIELD_MEMBERSHIPS: ClassVar[str] = "memberships"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    id: str
    name: str
    display_name: str

    # NOTE FOR ME:
    # Odpowiednik List<@Valid OrganizationMemberships> z @NotNull @NotEmpty:
    # - typ elementu listy = OrganizationMembershipsDto (dziedziczy po BaseDto)
    #   -> Pydantic waliduje KAŻDY element listy rekurencyjnie, automatycznie (odpowiednik @Valid na elemencie)
    # - min_length=1 -> odpowiednik @NotEmpty (lista musi mieć min. 1 element)
    # - brak Optional -> pole samo w sobie jest wymagane (odpowiednik @NotNull na całej liście)
    memberships: list[OrganizationMembershipsDto] = Field(min_length=1)

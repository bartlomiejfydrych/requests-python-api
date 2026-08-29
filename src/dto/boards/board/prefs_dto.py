from typing import Any, ClassVar, Optional

from pydantic import Field

from dto.base_dto import BaseDto
from dto.boards.board.prefs.switcher_view_dto import SwitcherViewDto


class PrefsDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_PERMISSION_LEVEL: ClassVar[str] = "permissionLevel"
    FIELD_HIDE_VOTES: ClassVar[str] = "hideVotes"
    FIELD_VOTING: ClassVar[str] = "voting"
    FIELD_COMMENTS: ClassVar[str] = "comments"
    FIELD_INVITATIONS: ClassVar[str] = "invitations"
    FIELD_SELF_JOIN: ClassVar[str] = "selfJoin"
    FIELD_CARD_COVERS: ClassVar[str] = "cardCovers"
    FIELD_SHOW_COMPLETE_STATUS: ClassVar[str] = "showCompleteStatus"
    FIELD_CARD_COUNTS: ClassVar[str] = "cardCounts"
    FIELD_IS_TEMPLATE: ClassVar[str] = "isTemplate"
    FIELD_CARD_AGING: ClassVar[str] = "cardAging"
    FIELD_CALENDAR_FEED_ENABLED: ClassVar[str] = "calendarFeedEnabled"
    FIELD_HIDDEN_PLUGIN_BOARD_BUTTONS: ClassVar[str] = "hiddenPluginBoardButtons"
    FIELD_SWITCHER_VIEWS: ClassVar[str] = "switcherViews"
    FIELD_AUTO_ARCHIVE: ClassVar[str] = "autoArchive"
    FIELD_BACKGROUND: ClassVar[str] = "background"
    FIELD_BACKGROUND_COLOR: ClassVar[str] = "backgroundColor"
    FIELD_BACKGROUND_DARK_COLOR: ClassVar[str] = "backgroundDarkColor"
    FIELD_BACKGROUND_IMAGE: ClassVar[str] = "backgroundImage"
    FIELD_BACKGROUND_DARK_IMAGE: ClassVar[str] = "backgroundDarkImage"
    FIELD_BACKGROUND_IMAGE_SCALED: ClassVar[str] = "backgroundImageScaled"
    FIELD_BACKGROUND_TILE: ClassVar[str] = "backgroundTile"
    FIELD_BACKGROUND_BRIGHTNESS: ClassVar[str] = "backgroundBrightness"
    FIELD_SHARED_SOURCE_URL: ClassVar[str] = "sharedSourceUrl"
    FIELD_BACKGROUND_BOTTOM_COLOR: ClassVar[str] = "backgroundBottomColor"
    FIELD_BACKGROUND_TOP_COLOR: ClassVar[str] = "backgroundTopColor"
    FIELD_CAN_BE_PUBLIC: ClassVar[str] = "canBePublic"
    FIELD_CAN_BE_ENTERPRISE: ClassVar[str] = "canBeEnterprise"
    FIELD_CAN_BE_ORG: ClassVar[str] = "canBeOrg"
    FIELD_CAN_BE_PRIVATE: ClassVar[str] = "canBePrivate"
    FIELD_CAN_INVITE: ClassVar[str] = "canInvite"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    # NOTE FOR ME:
    # @Pattern(regexp = "...") -> Field(pattern=r"...") - regex ograniczający dozwolone wartości stringa.

    permission_level: str = Field(pattern=r"^(org|private|public)$")
    hide_votes: bool
    voting: str = Field(pattern=r"^(disabled|members|observers|org|public)$")
    comments: str = Field(pattern=r"^(disabled|members|observers|org|public)$")
    invitations: str = Field(pattern=r"^(members|admins)$")

    self_join: bool
    card_covers: bool
    show_complete_status: bool
    card_counts: bool
    is_template: bool

    card_aging: str = Field(pattern=r"^(pirate|regular)$")

    calendar_feed_enabled: bool

    # NOTE FOR ME:
    # List<Object> z @NotNull (bez @Valid) -> list[Any], wymagane (lista musi istnieć,
    # ale jej elementy nie są dalej walidowane - odpowiednik braku @Valid na elemencie).
    hidden_plugin_board_buttons: list[Any]

    # NOTE FOR ME:
    # List<SwitcherView> - element ma zdefiniowany typ (SwitcherViewDto dziedziczy po BaseDto),
    # więc Pydantic waliduje każdy element automatycznie.
    switcher_views: list[SwitcherViewDto]

    # NOTE FOR ME:
    # Pola z @JsonProperty BEZ required=true i bez @NotNull w konstruktorze Javy -> Optional[Any] = None.
    # W Javie oznaczały "typ nieokreślony (Object), dopuszczalny brak/null".
    auto_archive: Optional[Any] = None

    background: str = Field(pattern=r"^(blue|orange|green|red|purple|pink|lime|sky|grey)$")

    background_color: str
    background_dark_color: Optional[Any] = None
    background_image: Optional[Any] = None
    background_dark_image: Optional[Any] = None
    background_image_scaled: Optional[Any] = None

    background_tile: bool
    background_brightness: str
    shared_source_url: Optional[Any] = None

    background_bottom_color: str
    background_top_color: str

    can_be_public: bool
    can_be_enterprise: bool
    can_be_org: bool
    can_be_private: bool
    can_invite: bool


'''
Rzeczy, na które chcę zwrócić uwagę

1. @Pattern(regexp = "org|private|public") → Field(pattern=r"^(org|private|public)$")
Zauważ, że dodałem ^(...)$ wokół oryginalnego regexu z Javy. To ważna różnica: java.util.regex.Pattern w Bean Validation
domyślnie sprawdza dopasowanie całego stringa (tak jakby ^ i $ były niejawnie dodane), natomiast Pythonowy re
(którego Pydantic używa pod spodem) domyślnie sprawdza tylko, czy wzorzec występuje gdziekolwiek w stringu
(re.search, nie re.fullmatch). Bez ^...$ regex org|private|public przepuściłby np. "organization"
(bo zawiera "org") — co w Javie zostałoby odrzucone. Dopisanie kotwic przywraca to samo zachowanie co w Javie.

2. Rozróżnienie Object wymagane vs. Object opcjonalne
To DTO ma trzy różne warianty pól typu Object w Javie, i każdy tłumaczy się inaczej:

– List<Object> hiddenPluginBoardButtons z @NotNull, jest w konstruktorze z required = true → list[Any] (wymagane, ale elementy nietypowane),
– Object autoArchive bez @NotNull, w konstruktorze bez required = true → Optional[Any] = None,
– podobnie backgroundDarkColor, backgroundImage, backgroundDarkImage, backgroundImageScaled, sharedSourceUrl — wszystkie bez @NotNull i bez required = true.

Czyli klucz to nie tylko typ (Object), ale czy pole ma @NotNull i required = true — to decyduje,
czy w Pythonie jest to Any (wymagane) czy Optional[Any] = None (opcjonalne).
'''

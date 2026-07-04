from enums.query_parameters.base_query_parameter import BaseQueryParameter


class PostCreateBoardQueryParameters(BaseQueryParameter):
    """
    NOTES FOR ME:
    Implementuje strukturalnie PostCreateBoardQueryParam
    (przez odziedziczone property {key} z BaseQueryParameter).
    """

    DEFAULT_LABELS = "defaultLabels"
    DEFAULT_LISTS = "defaultLists"
    ID_BOARD_SOURCE = "idBoardSource"
    KEEP_FROM_SOURCE = "keepFromSource"
    POWER_UPS = "powerUps"

    PREFS_PERMISSION_LEVEL = "prefs_permissionLevel"
    PREFS_VOTING = "prefs_voting"
    PREFS_COMMENTS = "prefs_comments"
    PREFS_INVITATIONS = "prefs_invitations"
    PREFS_SELF_JOIN = "prefs_selfJoin"
    PREFS_CARD_COVERS = "prefs_cardCovers"
    PREFS_BACKGROUND = "prefs_background"
    PREFS_CARD_AGING = "prefs_cardAging"

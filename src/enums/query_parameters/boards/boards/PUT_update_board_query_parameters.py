from enums.query_parameters.base_query_parameter import BaseQueryParameter


class PutUpdateBoardQueryParameters(BaseQueryParameter):
    # ==========================================================================================================
    # ENUMS
    # ==========================================================================================================

    CLOSED = "closed"
    SUBSCRIBED = "subscribed"

    PREFS_PERMISSION_LEVEL = "prefs/permissionLevel"
    PREFS_SELF_JOIN = "prefs/selfJoin"
    PREFS_CARD_COVERS = "prefs/cardCovers"
    PREFS_HIDE_VOTES = "prefs/hideVotes"
    PREFS_INVITATIONS = "prefs/invitations"
    PREFS_VOTING = "prefs/voting"
    PREFS_COMMENTS = "prefs/comments"
    PREFS_BACKGROUND = "prefs/background"
    PREFS_CARD_AGING = "prefs/cardAging"
    PREFS_CALENDAR_FEED_ENABLED = "prefs/calendarFeedEnabled"

from dataclasses import dataclass
from typing import Optional

from payloads.base_payload import BasePayload
from enums.query_parameters.boards.boards.board_base_query_parameters import BoardBaseQueryParameters as Base
from enums.query_parameters.boards.boards.PUT_update_board_query_parameters import \
    PutUpdateBoardQueryParameters as Put


@dataclass(kw_only=True)
class PutUpdateBoardPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    name: Optional[str] = None
    desc: Optional[str] = None
    closed: Optional[bool] = None
    subscribed: Optional[str] = None
    id_organization: Optional[str] = None
    prefs_permission_level: Optional[str] = None
    prefs_self_join: Optional[bool] = None
    prefs_card_covers: Optional[bool] = None
    prefs_hide_votes: Optional[bool] = None
    prefs_invitations: Optional[str] = None
    prefs_voting: Optional[str] = None
    prefs_comments: Optional[str] = None
    prefs_background: Optional[str] = None
    prefs_card_aging: Optional[str] = None
    prefs_calendar_feed_enabled: Optional[bool] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Base.DESC, self.desc)
        self.put_if_not_null(params, Put.CLOSED, self.closed)
        self.put_if_not_null(params, Put.SUBSCRIBED, self.subscribed)
        self.put_if_not_null(params, Base.ID_ORGANIZATION, self.id_organization)
        self.put_if_not_null(params, Put.PREFS_PERMISSION_LEVEL, self.prefs_permission_level)
        self.put_if_not_null(params, Put.PREFS_SELF_JOIN, self.prefs_self_join)
        self.put_if_not_null(params, Put.PREFS_CARD_COVERS, self.prefs_card_covers)
        self.put_if_not_null(params, Put.PREFS_HIDE_VOTES, self.prefs_hide_votes)
        self.put_if_not_null(params, Put.PREFS_INVITATIONS, self.prefs_invitations)
        self.put_if_not_null(params, Put.PREFS_VOTING, self.prefs_voting)
        self.put_if_not_null(params, Put.PREFS_COMMENTS, self.prefs_comments)
        self.put_if_not_null(params, Put.PREFS_BACKGROUND, self.prefs_background)
        self.put_if_not_null(params, Put.PREFS_CARD_AGING, self.prefs_card_aging)
        self.put_if_not_null(params, Put.PREFS_CALENDAR_FEED_ENABLED, self.prefs_calendar_feed_enabled)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PutUpdateBoardPayload(
#     name="Zmieniona tablica",
#     prefs_background="lime",
#     prefs_self_join=True,
#     prefs_card_aging="Błąd krytyczny",
# )
#
# query_params = payload.to_query_params()

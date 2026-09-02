from dataclasses import dataclass
from typing import Optional

from payloads.base_payload import BasePayload
from enums.query_parameters.boards.boards.board_base_query_parameters import BoardBaseQueryParameters as Base
from enums.query_parameters.boards.boards.POST_create_board_query_parameters import \
    PostCreateBoardQueryParameters as Post


@dataclass(kw_only=True)
class PostCreateBoardPayload(BasePayload):
    # ==========================================================================================================
    # FIELDS – QUERY PARAMETERS
    # ==========================================================================================================

    name: Optional[str] = None
    default_labels: Optional[bool] = None
    default_lists: Optional[bool] = None
    desc: Optional[str] = None
    id_organization: Optional[str] = None
    id_board_source: Optional[str] = None
    keep_from_source: Optional[str] = None
    power_ups: Optional[str] = None
    prefs_permission_level: Optional[str] = None
    prefs_voting: Optional[str] = None
    prefs_comments: Optional[str] = None
    prefs_invitations: Optional[str] = None
    prefs_self_join: Optional[bool] = None
    prefs_card_covers: Optional[bool] = None
    prefs_background: Optional[str] = None
    prefs_card_aging: Optional[str] = None

    # ==========================================================================================================
    # HELPER METHOD – CONVERTS THE PAYLOAD TO A QUERY PARAMETER DICT
    # ==========================================================================================================

    def to_query_params(self) -> dict:
        params: dict = {}

        self.put_if_not_null(params, Base.NAME, self.name)
        self.put_if_not_null(params, Post.DEFAULT_LABELS, self.default_labels)
        self.put_if_not_null(params, Post.DEFAULT_LISTS, self.default_lists)
        self.put_if_not_null(params, Base.DESC, self.desc)
        self.put_if_not_null(params, Base.ID_ORGANIZATION, self.id_organization)
        self.put_if_not_null(params, Post.ID_BOARD_SOURCE, self.id_board_source)
        self.put_if_not_null(params, Post.KEEP_FROM_SOURCE, self.keep_from_source)
        self.put_if_not_null(params, Post.POWER_UPS, self.power_ups)
        self.put_if_not_null(params, Post.PREFS_PERMISSION_LEVEL, self.prefs_permission_level)
        self.put_if_not_null(params, Post.PREFS_VOTING, self.prefs_voting)
        self.put_if_not_null(params, Post.PREFS_COMMENTS, self.prefs_comments)
        self.put_if_not_null(params, Post.PREFS_INVITATIONS, self.prefs_invitations)
        self.put_if_not_null(params, Post.PREFS_SELF_JOIN, self.prefs_self_join)
        self.put_if_not_null(params, Post.PREFS_CARD_COVERS, self.prefs_card_covers)
        self.put_if_not_null(params, Post.PREFS_BACKGROUND, self.prefs_background)
        self.put_if_not_null(params, Post.PREFS_CARD_AGING, self.prefs_card_aging)

        return params

# ==========================================================================================================
# EXAMPLE OF USE
# ==========================================================================================================

# payload = PostCreateBoardPayload(
#     name="Tablica API",
#     desc="Testowa tablica",
#     default_labels=False,
#     prefs_background="blue",
# )
#
# query_params = payload.to_query_params()

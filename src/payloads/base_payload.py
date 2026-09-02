from typing import Any

from enums.query_parameters.base_query_parameter import BaseQueryParameter


class BasePayload:

    # ==========================================================================================================
    # METHODS – MAIN
    # ==========================================================================================================

    @staticmethod
    def put_if_not_null(params: dict[str, Any], param: BaseQueryParameter, value: Any) -> None:
        if value is not None:
            # NOTE:
            # Python's str(True/False) -> "True"/"False", but Trello (like Java's
            # Boolean.toString()) expects lowercase "true"/"false". Without this,
            # requests would serialize bool query params with capitalized text,
            # which some Trello params (e.g. prefs_selfJoin) reject as invalid.
            if isinstance(value, bool):
                value = str(value).lower()
            params[param.key] = value

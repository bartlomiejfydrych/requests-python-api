from typing import Any

from src.enums.query_parameters.base_query_parameter import BaseQueryParameter


class BasePayload:

    # ==========================================================================================================
    # METHODS – MAIN
    # ==========================================================================================================

    @staticmethod
    def put_if_not_null(params: dict[str, Any], param: BaseQueryParameter, value: Any) -> None:
        if value is not None:
            params[param.key] = value

from enum import Enum


class LogsMode(Enum):

    # ==========================================================================================================
    # ENUMS
    # ==========================================================================================================

    OFF = "OFF"
    FULL = "FULL"
    SHORT = "SHORT"
    CUSTOM = "CUSTOM"

    # ==========================================================================================================
    # VALIDATOR
    # ==========================================================================================================

    @staticmethod
    def from_value(value: str) -> "LogsMode":
        try:
            return LogsMode[value.upper()]
        except KeyError:
            raise ValueError(
                f"(CONFIG) Invalid LOGS_MODE value: {value}. Allowed: OFF, FULL, SHORT, CUSTOM"
            )

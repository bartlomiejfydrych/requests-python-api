from enum import Enum


class BaseQueryParameter(Enum):
    """
    NOTES FOR ME:
    Wspólna baza dla wszystkich enumów z query parametrami.
    Zastępuje powtarzanie property {key} w każdym enumie osobno
    (W Javie każdy enum musiał to robić sam, bo implementował interfejs).
    """

    @property
    def key(self) -> str:
        return self.value

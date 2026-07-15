from pydantic import BaseModel, ConfigDict


class BaseDto(BaseModel):
    """
    NOTE FOR ME:
    Odpowiednik ProviderObjectMapper z Javy (Jackson ObjectMapper).

    Różnica: w Jacksonie konfiguracja żyła w jednym globalnym obiekcie
    ObjectMapper, używanym do wszystkich deserializacji.
    W Pydantic konfiguracja jest przypisana do KLASY modelu i dziedziczy się
    przez wspólną klasę bazową - każdy DTO w projekcie powinien dziedziczyć
    po BaseDto zamiast bezpośrednio po BaseModel.

    extra="forbid"  -> FAIL_ON_UNKNOWN_PROPERTIES
                        (nadmiarowe pole w JSON = błąd)

    strict=True     -> blokuje niejawną koercję typów, m.in.:
                        int/float/bool -> str (to co ręcznie konfigurowałeś
                        przez coercionConfigFor(LogicalType.Textual))
                        a także str -> int/float/bool w drugą stronę

    (brak explicit "FAIL_ON_MISSING") -> pole bez wartości domyślnej jest
                        w Pydantic zawsze wymagane, więc odpowiednik
                        FAIL_ON_MISSING_CREATOR_PROPERTIES działa "z automatu"
                        i nie trzeba go włączać

    (brak explicit "FAIL_ON_NULL_FOR_PRIMITIVES") -> pole typu int/bool/float
                        (bez Optional) domyślnie NIE akceptuje None,
                        więc to również działa "z automatu"
    """

    model_config = ConfigDict(
        extra="forbid",
        strict=True,
    )

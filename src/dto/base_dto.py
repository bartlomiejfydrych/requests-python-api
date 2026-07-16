from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


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

    alias_generator=to_camel -> odpowiednik globalnego PropertyNamingStrategy
                        z Jacksona. Pola w Pythonie piszemy w snake_case
                        (zgodnie z PEP 8), a Pydantic SAM generuje alias
                        camelCase używany przy parsowaniu JSON-a z API.
                        Np. pole "id_organization" -> alias "idOrganization".
                        Dzięki temu NIE trzeba ręcznie dopisywać
                        Field(alias="...") do każdego pola z osobna.

    populate_by_name=True -> pozwala tworzyć obiekt w kodzie Python
                        PO NAZWIE POLA (snake_case), a nie tylko po aliasie
                        (camelCase). Bez tego np. BoardBaseDto(id_organization=...)
                        rzuciłoby błąd walidacji - trzeba by pisać
                        BoardBaseDto(idOrganization=...), co byłoby niezgodne
                        z konwencją reszty projektu.

    (brak explicit "FAIL_ON_MISSING") -> pole bez wartości domyślnej jest
                        w Pydantic zawsze wymagane, więc odpowiednik
                        FAIL_ON_MISSING_CREATOR_PROPERTIES działa "z automatu"
                        i nie trzeba go włączać

    (brak explicit "FAIL_ON_NULL_FOR_PRIMITIVES") -> pole typu int/bool/float
                        (bez Optional) domyślnie NIE akceptuje None,
                        więc to również działa "z automatu"

    Jedna pułapka, na którą warto uważać:
    to_camel zamienia id → id (bez zmian, bo nie ma podkreślnika) i url → url — to spoko. Ale uważaj na pola,
    masz akronimy albo cyfry w nazwie (np. gdyby było id2 czy url_v2) — to_camel czasem generuje nieoczekiwane wyniki
    przy takich przypadkach brzegowych. W tym konkretnym DTO nie masz takich pól, więc jesteś bezpieczny, ale warto
    to mieć z tyłu głowy przy kolejnych DTO z Trello API (np. pola z 2 w nazwie).
    """

    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        alias_generator=to_camel,
        populate_by_name=True,
    )

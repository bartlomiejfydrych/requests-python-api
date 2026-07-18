from typing import ClassVar

from dto.base_dto import BaseDto


class LabelNamesDto(BaseDto):
    # ==========================================================================================================
    # FIELD NAME CONSTANTS
    # ==========================================================================================================

    FIELD_GREEN: ClassVar[str] = "green"
    FIELD_YELLOW: ClassVar[str] = "yellow"
    FIELD_ORANGE: ClassVar[str] = "orange"
    FIELD_RED: ClassVar[str] = "red"
    FIELD_PURPLE: ClassVar[str] = "purple"
    FIELD_BLUE: ClassVar[str] = "blue"
    FIELD_SKY: ClassVar[str] = "sky"
    FIELD_LIME: ClassVar[str] = "lime"
    FIELD_PINK: ClassVar[str] = "pink"
    FIELD_BLACK: ClassVar[str] = "black"

    FIELD_GREEN_DARK: ClassVar[str] = "green_dark"
    FIELD_YELLOW_DARK: ClassVar[str] = "yellow_dark"
    FIELD_ORANGE_DARK: ClassVar[str] = "orange_dark"
    FIELD_RED_DARK: ClassVar[str] = "red_dark"
    FIELD_PURPLE_DARK: ClassVar[str] = "purple_dark"
    FIELD_BLUE_DARK: ClassVar[str] = "blue_dark"
    FIELD_SKY_DARK: ClassVar[str] = "sky_dark"
    FIELD_LIME_DARK: ClassVar[str] = "lime_dark"
    FIELD_PINK_DARK: ClassVar[str] = "pink_dark"
    FIELD_BLACK_DARK: ClassVar[str] = "black_dark"

    FIELD_GREEN_LIGHT: ClassVar[str] = "green_light"
    FIELD_YELLOW_LIGHT: ClassVar[str] = "yellow_light"
    FIELD_ORANGE_LIGHT: ClassVar[str] = "orange_light"
    FIELD_RED_LIGHT: ClassVar[str] = "red_light"
    FIELD_PURPLE_LIGHT: ClassVar[str] = "purple_light"
    FIELD_BLUE_LIGHT: ClassVar[str] = "blue_light"
    FIELD_SKY_LIGHT: ClassVar[str] = "sky_light"
    FIELD_LIME_LIGHT: ClassVar[str] = "lime_light"
    FIELD_PINK_LIGHT: ClassVar[str] = "pink_light"
    FIELD_BLACK_LIGHT: ClassVar[str] = "black_light"

    # ==========================================================================================================
    # FIELDS – VALIDATION CONSTRAINTS
    # ==========================================================================================================

    green: str
    yellow: str
    orange: str
    red: str
    purple: str
    blue: str
    sky: str
    lime: str
    pink: str
    black: str

    green_dark: str
    yellow_dark: str
    orange_dark: str
    red_dark: str
    purple_dark: str
    blue_dark: str
    sky_dark: str
    lime_dark: str
    pink_dark: str
    black_dark: str

    green_light: str
    yellow_light: str
    orange_light: str
    red_light: str
    purple_light: str
    blue_light: str
    sky_light: str
    lime_light: str
    pink_light: str
    black_light: str

'''
Ważna pułapka, którą to DTO ujawnia

Zwróć uwagę na coś nietypowego: w Javie pole greenDark (camelCase) mapowało się przez @JsonProperty(value = "green_dark")
na klucz JSON w snake_case. To odwrotna sytuacja niż we wszystkich poprzednich DTO — tu JSON od Trello już jest
w snake_case, a nie w camelCase.
Gdybyś to zignorował i po prostu napisał green_dark: str licząc na globalny alias_generator=to_camel z BaseDto,
to wygenerowałby on alias greenDark — czyli niezgodny z prawdziwym kluczem JSON (green_dark). Deserializacja by się wysypała.
Dlaczego mimo to powyższy kod działa poprawnie, bez żadnych zmian w BaseDto? Dzięki populate_by_name=True,
które dodaliśmy wcześniej z zupełnie innego powodu (ręczna mutacja/konstrukcja obiektów). Ta flaga ma dodatkowy,
bardzo przydatny tu efekt uboczny: pozwala Pydantic dopasować dane wejściowe zarówno po aliasie, jak i po dosłownej nazwie pola.

Czyli:
pole green_dark ma wygenerowany alias greenDark (przez to_camel),
ale JSON z kluczem "green_dark" też się dopasuje — bo populate_by_name=True akceptuje dosłowną nazwę pola Python jako alternatywną ścieżkę dopasowania,
więc oba warianty (greenDark i green_dark) są jednocześnie poprawne przy model_validate().

To znaczy, że nie musisz nic specjalnie obsługiwać dla tego przypadku — mechanizm, który dodaliśmy wcześniej dla zupełnie
innego celu, przy okazji zabezpiecza Cię też przed tą niespójnością nazewnictwa w API Trello. Ale warto to mieć świadomie
z tyłu głowy, bo to nieoczywiste zachowanie.
'''

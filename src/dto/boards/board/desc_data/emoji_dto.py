from dto.base_dto import BaseDto


class EmojiDto(BaseDto):
    """
    NOTE FOR ME:
    Pusta klasa - odpowiednik Emoji.java bez żadnych pól.
    Dzięki odziedziczonemu z BaseDto extra="forbid", to DTO akceptuje TYLKO pusty obiekt {}
    w JSON-ie. Jakikolwiek klucz w środku (nawet jeden) zostanie odrzucony jako "nieznane pole" -
    dokładnie tak jak w Javie z @JsonIgnoreProperties(ignoreUnknown = false) na klasie bez pól.
    """
    pass

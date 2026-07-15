class ExceptionDtoDeserialization(Exception):
    """
    NOTE FOR ME:
    Odpowiednik połączonych ExceptionJsonDeserialization + ExceptionDtoValidation
    z Javy.

    W Pydantic nie da się czysto rozdzielić błędów strukturalnych
    (brakujące/nadmiarowe pole, zły typ) od błędów walidacji biznesowej
    (np. Field(min_length=1)) - obie kategorie są zwracane przez ten sam
    wyjątek pydantic.ValidationError w jednym przebiegu walidatora.
    Dlatego oba przypadki opakowuję w jeden wyjątek domenowy.
    """
    pass

"""
NOTE FOR ME:
Funkcja UtilsRandom.pickRandom(T...) w Javie ma 2 oddzielne przypadki negatywne (tablica argumentów zmiennych
o wartości null vs. pusta tablica argumentów zmiennych), ponieważ w Javie są to 2 różne sposoby wywołania metody (pickRandom((String[]) null) vs.
pickRandom()). W Pythonie *options jest zawsze zbierane w krotkę — nie ma możliwości przekazania „null” jako
samej zmiennej, więc wywołanie pick_random() bez argumentów jest jedynym sposobem na wywołanie przypadku
„brak podanych opcji”, a oba przypadki w Javie łączą się tutaj w jeden test.

Funkcja pickRandom(List<T>) w Javie jest odwzorowana na pick_random_from_sequence(Sequence[T]) w Pythonie, która AKCEPTUJE
None jako jawny argument (w przeciwieństwie do *options), więc zarówno przypadek „None”, jak i „empty” są rozdzielone,
tak samo jak w Javie.
"""

import pytest

from utils.utils_random import pick_random, pick_random_from_sequence


@pytest.mark.unit
class TestUtilsRandom:
    # ==========================================================================================================
    # pick_random(*options)
    # ==========================================================================================================

    def test_pick_random_when_no_options_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            pick_random()

    def test_pick_random_when_valid_options_should_return_one_of_them(self) -> None:
        a, b, c = "A", "B", "C"

        result = pick_random(a, b, c)

        assert result in (a, b, c), "Returned value must be one of provided options"

    # ==========================================================================================================
    # pick_random_from_sequence(options)
    # ==========================================================================================================

    def test_pick_random_from_sequence_when_none_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            # noinspection PyTypeChecker
            pick_random_from_sequence(None)

    def test_pick_random_from_sequence_when_empty_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            pick_random_from_sequence([])

    def test_pick_random_from_sequence_when_valid_options_should_return_one_of_them(self) -> None:
        options = [1, 2, 3, 4, 5]

        result = pick_random_from_sequence(options)

        assert result in options, "Returned value must be one of provided options"

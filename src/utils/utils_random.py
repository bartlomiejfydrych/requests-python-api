from enum import Enum
from typing import Sequence, Type, TypeVar

from providers.provider_random import random

T = TypeVar("T")
E = TypeVar("E", bound=Enum)


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# NOTE FOR ME: W Javie były dwa przeciążenia (varargs i List<T>) — czysty language workaround,
# w Pythonie jedna funkcja przyjmująca Sequence (list, tuple, ...) pokrywa oba przypadki.

def pick_random(options: Sequence[T]) -> T:
    if not options:
        raise ValueError("pick_random() requires at least one option")
    return options[random().randrange(len(options))]


# EXAMPLE OF USE:
# color: BoardColor = pick_random_enum(BoardColor)

def pick_random_enum(enum_class: Type[E]) -> E:
    return pick_random(list(enum_class))

from collections.abc import Sequence
from enum import Enum
from typing import TypeVar

from providers.provider_random import random

T = TypeVar("T")
E = TypeVar("E", bound=Enum)


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# -------------------------
# PICK RANDOM FROM ARGUMENTS
# -------------------------

def pick_random(*options: T) -> T:
    if not options:
        raise ValueError("pick_random() requires at least one option")

    return options[random().randrange(len(options))]


# --------------------------
# PICK RANDOM FROM SEQUENCE
# --------------------------

def pick_random_from_sequence(options: Sequence[T]) -> T:
    if not options:
        raise ValueError("pick_random_from_sequence() requires at least one option")

    return options[random().randrange(len(options))]


# ----------------------
# PICK RANDOM ENUM VALUE
# ----------------------

# EXAMPLE OF USE:
# color: BoardColor = pick_random_enum(BoardColor)

def pick_random_enum(enum_class: type[E]) -> E:
    return pick_random_from_sequence(list(enum_class))

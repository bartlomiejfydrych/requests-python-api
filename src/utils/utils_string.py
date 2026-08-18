from providers.provider_random import random

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

_ALPHANUMERIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# NOTE: Znak "%" musiał zostać usunięty, ponieważ dla kombinacji "%Y" dekoder REST Assured w Javie rzucał
# wyjątkiem (URLDecoder: Illegal hex characters in escape (%) pattern). Zachowane 1:1 również w Pythonie,
# mimo że dekoder może być inny — dla spójności danych testowych między obiema wersjami frameworka.
_ALL_CHARACTERS = (
    "!\"#$&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`"
    "abcdefghijklmnopqrstuvwxyz{|}~ ęĘóÓąĄśŚłŁżŻźŹćĆńŃ"
)

_ENCODED_SPECIAL_CHARS: list[str] = [
    "%2F", "%3F", "%23", "%3C", "%3E",
    "%22", "%27", "%7B", "%7D", "%5B", "%5D", "%25",
]


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def get_random_single_char(allowed_chars: str) -> str:
    if not allowed_chars:
        raise ValueError("Allowed characters cannot be empty")
    return random().choice(allowed_chars)


def get_random_single_char_alphanumeric() -> str:
    return get_random_single_char(_ALPHANUMERIC)


def get_all_characters_set_in_random_order() -> str:
    return _shuffle_characters(_ALL_CHARACTERS)


def get_all_encoded_special_characters_in_random_order() -> str:
    shuffled: list[str] = _ENCODED_SPECIAL_CHARS.copy()
    random().shuffle(shuffled)
    return "".join(shuffled)


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

def _shuffle_characters(input_string: str) -> str:
    chars: list[str] = list(input_string)
    random().shuffle(chars)
    return "".join(chars)

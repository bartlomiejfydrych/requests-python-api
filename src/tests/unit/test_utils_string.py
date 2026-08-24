import re

import pytest

from utils.utils_string import (
    get_all_characters_set_in_random_order,
    get_all_encoded_special_characters_in_random_order,
    get_random_single_char,
    get_random_single_char_alphanumeric,
)


@pytest.mark.unit
class TestUtilsString:
    # ==========================================================================================================
    # get_random_single_char(allowed_chars)
    # ==========================================================================================================

    def test_get_random_single_char_when_none_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            # noinspection PyTypeChecker
            get_random_single_char(None)

    def test_get_random_single_char_when_empty_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            get_random_single_char("")

    def test_get_random_single_char_when_valid_chars_should_return_single_allowed_char(self) -> None:
        allowed = "ABC123"

        result = get_random_single_char(allowed)

        assert len(result) == 1
        assert result in allowed, "Returned character must be from allowed set"

    # ==========================================================================================================
    # get_random_single_char_alphanumeric()
    # ==========================================================================================================

    def test_get_random_single_char_alphanumeric_should_return_single_alphanumeric_char(self) -> None:
        result = get_random_single_char_alphanumeric()

        assert len(result) == 1
        assert re.fullmatch(r"[A-Za-z0-9]", result) is not None, "Returned character must be alphanumeric"

    # ==========================================================================================================
    # get_all_characters_set_in_random_order()
    # ==========================================================================================================

    def test_get_all_characters_set_in_random_order_should_contain_same_characters(self) -> None:
        original = (
            "!\"#$&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`"
            "abcdefghijklmnopqrstuvwxyz{|}~ ęĘóÓąĄśŚłŁżŻźŹćĆńŃ"
        )

        shuffled = get_all_characters_set_in_random_order()

        assert len(shuffled) == len(original)
        assert set(shuffled) == set(original), "Shuffled string must contain exactly the same characters"

    # ==========================================================================================================
    # get_all_encoded_special_characters_in_random_order()
    # ==========================================================================================================

    def test_get_all_encoded_special_characters_in_random_order_should_contain_all_encoded_values(self) -> None:
        result = get_all_encoded_special_characters_in_random_order()

        expected = [
            "%2F", "%3F", "%23", "%3C", "%3E",
            "%22", "%27", "%7B", "%7D", "%5B", "%5D", "%25",
        ]

        for encoded in expected:
            assert encoded in result, f"Result should contain encoded value: {encoded}"

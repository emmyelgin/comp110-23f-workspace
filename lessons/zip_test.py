"""Test my zip function."""

from lessons.zip import zip

_author_ = "730464992"


def test_empty_zip() -> None: 
    """Testing on empty lists as parameters."""
    assert zip([], []) == {}


def test_zip_length_two() -> None:
    """Testing lists of length two."""
    assert zip(["power", "weak"], [1, 2]) == {"power": 1, "weak": 2}


def test_zip_neg_and_pos() -> None:
    """Testing negative and positive list."""
    word_list: list[str] = ["p", "a", "e", "l"]
    num_list: list[int] = [1, -5, 6, -8]
    assert zip(word_list, num_list) == {"p": 1, "a": -5, "e": 6, "l": -8}
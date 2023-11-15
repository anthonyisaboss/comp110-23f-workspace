"""Test my zip function."""

__author__ = "730669473"

from lessons.zip import zip


def test_empty_list() -> None:
    """Going to test empty function."""
    assert zip([], []) == {}


def test_elem() -> None:
    """Testing for on element."""
    first_test: dict[str, int] = {"Hi": 2}
    first: list[str] = ["Hi"]
    second: list[int] = [2]
    assert zip(first, second) == first_test


def test_two_elem() -> None:
    """Testing two elements."""
    second_test: dict[str, int] = {"Hi": 2, "goodbye": 3}
    first: list[str, str] = ["Hi", "goodbye"]
    second: list[int] = [2, 3]
    assert zip(first, second) == second_test

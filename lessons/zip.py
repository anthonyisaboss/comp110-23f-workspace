"""Combining two lists into a dictionary."""

__author__ = "730669473"


def zip(string: list[str], integer: list[int]) -> dict[str, int]:
    """Going to return a string and an int."""
    dict_list: dict[str, int] = {}
    if len(string) != len(integer):
        return dict_list
    idx: int = 0
    alt_idx: int = 0
    while idx < len(integer):
        dict_list[string[idx]] = integer[alt_idx]
        idx += 1
        alt_idx += 1
    return dict_list
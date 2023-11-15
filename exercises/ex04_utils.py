"""This is list practice."""
__author__ = "730669473"


def all(contained: list[int], num: int) -> bool:
    """This is going to show you if the numbers match."""
    idx: int = 0
    if len(contained) == 0:
        return False
    while idx < len(contained):
        if contained[idx] == num:
            idx += 1
        else:
            return False
    return True


def max(contained: list[int]) -> int:
    """Going to return the max number."""
    idx: int = 1
    if len(contained) == 0:
        raise ValueError("max() arg is an empty list")
    maximum = contained[0]
    while idx < len(contained):
        if contained[idx] > maximum:
            maximum = contained[idx]
        idx += 1
    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Going to tell you if the numbers are equal."""
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx += 1
        else:  
            return False
    return True

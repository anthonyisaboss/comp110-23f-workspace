"""TEsting my sum of evens function."""

from lessons.sum_evens import sum_evens_of_list

def test_empty_list() -> None:
    """Testing nothing"""
    assert sum_evens_of_list([]) == 0

def test_sum_one_element() -> None:
    """sum_evens_of_list([2])"""
    test_list: list[int] = [2]
    assert sum_evens_of_list(test_list) == 2

def test_sum_positive () -> None:
    """Sum_evens_of_list testing positive numbers."""
    test_list: list[int] = [1,2,3,4]
    assert sum_evens_of_list(test_list) == 6

def test_sum_neg_and_positives() -> None:
    """sum of list with negative andd positive"""
    test_list: list[int] = [-1,-2,3,4]
    assert sum_evens_of_list(test_list) == 2
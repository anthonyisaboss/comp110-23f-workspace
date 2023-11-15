"""This is going to be sums."""
__author__ = "730669473"


def w_sum(vals: list[float]) -> float:
    """This is going to create a list of numbers."""
    idx: int = 0
    sum: float = 0.0   
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(rad: list[float]) -> float:
    """Giving you the adding using for."""
    add: float = 0.0
    for elem in rad:
        add += elem
    return add


def f_range_sum(spad: list[float]) -> float:
    """Adding elements with range."""
    elem: float = 0
    for idx in range(0, len(spad)):
        elem += spad[idx]
    return elem
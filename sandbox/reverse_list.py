"""Going to reverse a list."""


def reverse_list(list1: list[str]) -> list[str]:
    """Going tot reverse a list"""
    list2: list[str] = []
    idx: int = len(list1) - 1
    while idx >= 0:
        list2.append(list1[idx])
        idx -= 1
    return list2


my_list = ["apple", "banana", "cherry", "date"]
reversed_list = reverse_list(my_list)
print(reversed_list)

    
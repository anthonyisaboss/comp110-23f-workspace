"""Odd and even practice."""

def odd_and_even(List1: list[int]) -> int:
    """Going too check indexes for odd and even"""

    list2: list[int] = []
    for elem in List1:
        if List1[elem] % 2 == 1 and elem % 2 == 0:
            list2.append(List1[elem])
    return list2

print(odd_and_even([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))




"""Exercise six dictionary."""

__author__ = "730669473"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Going to invert a dict."""
    dict2: dict[str, str] = {}
    for elem in dict1:
        dict2[dict1[elem]] = elem
    if len(dict1) != len(dict2):
        raise KeyError("You cannot have more than 1 of same key!")
    return dict2
        
    
def favorite_color(dict1: dict[str, str]) -> str:
    """Going to return the most popular color."""
    dict2: dict[str, int] = {}
    for elem in dict1:
        if dict1[elem] in dict2:
            dict2[dict1[elem]] += 1
        else:
            dict2[dict1[elem]] = 1
    count: int = 0
    for val in dict2:
        if dict2[val] > count:
            count = dict2[val]
    for color in dict2:
        if dict2[color] == count:
            return color
    return "blue"


def count(list1: list[str]) -> dict[str, int]:
    """Going to define a function to coun."""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Going to search through idx and find the first letter."""
    dict1 = {}
    for elem in list1:
        if elem[0].lower() not in dict1:
            dict1[elem[0].lower()] = [elem]
        else: 
            dict1[elem[0].lower()].append(elem)
    return dict1


def update_attendance(dict1: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    """Going to update the attendance of the class."""
    if week_day not in dict1:
        dict1[week_day] = [student]
    
    else: 
        if student not in dict1[week_day]:
            dict1[week_day].append(student)
        
    return dict1
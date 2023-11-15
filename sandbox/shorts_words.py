"""Short word practice"""


def short_words(list1: list[str]) -> list[str]:
    """Letting you know if the word is too long"""
    list2: list[str] = []
    for elem in list1:
        if len(elem) < 5:
            list2.append(elem)
        else:
            print(f"{elem} is too long!")
    return list2

list1 = [ "sun" , "cloud" , "sky" ]
print(short_words(list1))


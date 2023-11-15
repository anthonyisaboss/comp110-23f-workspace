"""Checking to see if a value exists."""

def value_exists(Dict1: dict[str,  int], val: int ) -> bool:
    """going to check if a value exists in a function"""
    exists: bool = False
    for elem in Dict1:
        if  Dict1[elem] == val:
            exists = True
            return exists
    return exists
    

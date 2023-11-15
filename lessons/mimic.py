"""mimic function"""

def  mimic ( my_words:str , letter: int) -> str:
    """outputs the character of my_words at leter_idx"""
    if letter >= len(my_words):
        return("Index tooo high")
    return my_words[letter]

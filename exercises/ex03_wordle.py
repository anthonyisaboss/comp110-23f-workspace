"""This is my wordle for comp 110!"""

__author__: "730669473"


def contains_char(word: str , guess_lettter: str) -> bool:
    """The purpose of this function is to guess which letter is being guessed."""
    assert len(guess_lettter) == 1
    to_count: int = 0
    real: bool = False
    while not real and to_count < len(word):
        if word[to_count] == guess_lettter:
            real = True
        to_count = to_count + 1
    return real
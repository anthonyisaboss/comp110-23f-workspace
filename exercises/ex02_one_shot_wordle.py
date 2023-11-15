"""One shot Wordle."""

__author__ = "730669473"
secret_word: str = ("python")
guess: str = input("What is your 6-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")  # this is for when the length of the guess is not equal to 6
number: int = 0  # counting variable
guessed: bool = False  #  boolean in order to make the boxes show up yellow or white
while number < len(guess):
    character = guess[number]  #  Variable in order to show what letter is being spoken to.
    if secret_word[number] == character:
        print((GREEN_BOX), end="")  
    else:
        guessed = True  #  boolean set to true in order to print colored boxes
        inside: bool = False  #  boolean in order to show if the letter is inside the secret word.
        random: int = 0
        while random < len(guess):
            if character == secret_word[random]:  # to see if the letter being addressed is inside the secret word.
                inside = True
            random += 1 
        if inside: # print yellow box if inside.
            print(YELLOW_BOX, end="" )  
        else:  # print white box if not inside.
            print(WHITE_BOX, end="")  
    number += 1 # add one to number in order for it not to loop
if guess == secret_word:  # great job ;)
   print(" Woo! You got it!") 
if guess != secret_word:
    print(" Not quite. Play again soon!") # awww trying again
"""This is going to be a guessing game"""

from random import randint
guess: int = int(input("guess a number between 1 and 10: "))
secret: int = randint(1,10)
guesses: int = 1
max_guess: int = 3

while (guess != secret) and (guesses < max_guess):
    print("wrong!")
    if (guess < 1 or guess > 10):
        print("Thats not between 1 and 10")
    if guess < secret:
        print("too low")
    if guess > secret:
        print("too high")
    guess = int(input("guess again: "))
    guesses += 1
    print(" you have" + guesses "left")
#if I've reached this point, guess == secret
if guess == secret:
    print("you guessed correctly")
else:
    print("You lose. :(" )
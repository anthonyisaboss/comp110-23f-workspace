"""Chardle worlde."""

__author__ = "730969476"
guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5:
    print("Error: Word must contain 5 characters") 
    exit()
guess_letter: str = input("Enter a single character: ")
if len(guess_letter) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + guess_letter + " in " + guess_word)
 
instances: int = 0
if str(guess_word[0]) == guess_letter:
    print(guess_letter + " found at index 0")
    instances = instances + 1
if str(guess_word[1]) == guess_letter:
    print(guess_letter + " found at index 1")
    instances = instances + 1
if str(guess_word[2]) == guess_letter:
    print(guess_letter + " found at index 2")
    instances = instances + 1
if str(guess_word[3]) == guess_letter:
    print(guess_letter + " found at index 3")
    instances = instances + 1
if str(guess_word[4]) == guess_letter:
    print(guess_letter + " found at index 4")
    instances = instances + 1
if int(instances) == 0:
    print("No instances of " + guess_letter + " found in " + guess_word)
if int(instances) == 1:
    print(str(instances) + " instance of " + guess_letter + " found in " + guess_word)
if int(instances) == 2:
    print(str(instances) + " instances of " + guess_letter + " found in " + guess_word)
if int(instances) == 3:
    print(str(instances) + " instances of " + guess_letter + " found in " + guess_word)
if int(instances) == 4:
    print(str(instances) + " instances of " + guess_letter + " found in " + guess_word)
if int(instances) == 5:
    print(str(instances) + " instances of " + guess_letter + " found in " + guess_word) 
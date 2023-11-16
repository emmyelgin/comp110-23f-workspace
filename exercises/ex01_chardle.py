"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730464992"
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
letter_counter: int = 0
print("Searching for " + letter + " in " + word) 

if letter == word[0]:
    print(letter + " found at index 0")
    letter_counter = letter_counter + 1
if letter == word[1]:
    print(letter + " found at index 1")
    letter_counter = letter_counter + 1
if letter == word[2]:
    print(letter + " found at index 2")
    letter_counter = letter_counter + 1
if letter == word[3]:
    print(letter + " found at index 3")
    letter_counter = letter_counter + 1
if letter == word[4]:
    print(letter + " found at index 4")
    letter_counter = letter_counter + 1

if letter_counter == 1: 
    print(str(letter_counter) + " instance of " + letter + " found in " + word)
elif letter_counter > 1: 
    print(str(letter_counter) + " instances of " + letter + " found in " + word)
else: 
    print("No instances of " + letter + " found in " + word)
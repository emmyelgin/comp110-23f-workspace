"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730464992" 
guess: str = input("What is your 6-letter guess? ")
secret: str = "python"
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
answer: str = ""
i: int = 0
idx: int = 0

# make sure guess is the legnth of the secret word 
while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")
while i < len(secret):
    # if letter is in correct spot add green box 
    if guess[i] == secret[i]:
        answer += green_box
    else:
        # if letter is in wrong spot add yellow box
        while idx < len(secret):
            if guess[i] == secret[idx]:
                answer += yellow_box
            idx = idx + 1
        # if no green or yellow box hasn't already been added, add white box
        if len(answer) <= i:
            answer += white_box
    i = i + 1
    idx = 0
print(answer)
if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
    


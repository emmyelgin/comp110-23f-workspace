"""EX03 - Structured Wordle."""

__author__: "730464992"


def contains_char(search_string, single_character) -> bool: 
    """Searching the search string for the single character."""
    assert len(single_character) == 1
    i: int = 0
    while i < len(search_string):
        if search_string[i] == single_character: 
            return True
        i = i + 1
    return False


def emojified(guess, secret) -> str:
    """Returning a codified string based on positioning and overlap of the letters
    in guess and secret."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    answer: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            answer += green_box
        elif contains_char(secret, guess[i]): 
            answer += yellow_box
        else:
            answer += white_box
        i = i + 1
    return answer


def input_guess(expected_length) -> str:
    """Return the users guess of expected length."""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    max_turns: int = 6
    winner: bool = False
    while turn <= max_turns and not winner:
        print("=== Turn " + str(turn) + "/" + str(max_turns) + " === ")
        user_guess: str = input_guess(len(secret))
        codified_string: str = emojified(user_guess, secret)
        print(codified_string)
        if user_guess == secret: 
            winner = True 
        turn = turn + 1
    if winner:
        print("You won in " + str(turn - 1) + "/" + str(max_turns) + " turns! ") 
    else:
        print("X/" + str(max_turns) + " - Sorry, try again tomorrow!")
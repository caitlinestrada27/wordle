"""Structured Wordle!"""

def contains_char(secret: str, guess: str) -> bool: 
    """Function to determine if secret word contains guess character anywhere."""
    # Check that second parameter is 1 character only
    assert len(guess) == 1
    # Check is character exists elsewhere in word 
    exists_in_word: bool = False
    idx: int = 0
    alt_idx: int = 0
    while ((exists_in_word is False) and (alt_idx < len(secret))):
        if (guess[idx] == secret[alt_idx]):
            exists_in_word = True
        else:
            alt_idx += 1
    idx += 1
    return exists_in_word


def emojified(guess: str, secret: str) -> str:
    """Function to return corresponding green, yellow, and white boxes for secret and guess."""
    # Check that guess and secret are equal in length 
    assert len(guess) == len(secret)
    idx: int = 0
    output: str = ""
    # Define emojis 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while (idx < len(secret)):
        if (guess[idx] == secret[idx]):
            output += GREEN_BOX
        elif (contains_char(secret, guess[idx]) is True):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        idx += 1
    return output 


def input_guess(expected_length: int) -> str:
    """Function to assign input to guess if input is expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while (len(guess) != expected_length):
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


# Main function to run Wordle 
def main() -> None: 
    """The entrypoint of the program and main game loop."""
    # Necessary variables to keep track of 
    secret_word: str = "codes"
    user_guess: str = ""
    max_turns: int = 6
    user_turns: int = 1
    game_won: bool = False
    # Run until user turns > max turns or game is won 
    while (user_turns <= max_turns and game_won is False):
        print(f"=== Turn {user_turns}/{max_turns} ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if (user_guess == secret_word):
            print(f"You won in {user_turns}/{max_turns} turns!")
            game_won = True
        user_turns += 1
    print(f"X/{max_turns} - Sorry, try again tomorrow!")


# Code Snippet - function becomes module & importable by other modules 
if __name__ == "__main__":
    main()
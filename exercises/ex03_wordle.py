"""My Wordle game for exercise 03 in COMP 110."""
__author__: str = "730661618"


def contains_char(secret: str, guess_letter: str) -> bool:
    """This function checks if a letter from the guess word is in the secret word."""
    assert len(guess_letter) == 1
    index_secret: int = 0
    while index_secret < len(secret):
        if secret[index_secret] == guess_letter:
            return True
        index_secret += 1
    return False 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" 


def emojified(guess: str, secret: str) -> str:
    """This function will visually show the green, yellow, and white boxes for the user to see where their guess letters stand in the secret word."""
    """Also ensures that guess word is same length as secret word."""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ""
    if secret == guess:
        emoji += (GREEN_BOX * len(guess))
        return emoji
    else:
        while i < len(secret):
            if guess[i] == secret[i]:
                emoji += GREEN_BOX
            elif contains_char(secret, guess[i]) is True:
                emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
            i += 1
        return emoji
    

def input_guess(expected_len: int) -> str:
    """This function allows for a user to input a guess word that should be the same length of the secret word's length."""
    guess = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    print(f"=== Turn {turn}/6 ===")
    guess = input_guess(len(secret))
    while turn <= 6:
        if guess == secret: 
            print(emojified(guess, secret)) 
            print(f"You won in {turn}/6 turns!")
            return
        else:
            print(emojified(guess, secret))

        turn += 1

        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            return
        
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))


if __name__ == "__main__":
    main()
"""My one shot wordle for ex02!"""
__author__: str = "730661618"

secretword: str = "python"
guess: str = input(f"What is your {len(secretword)}-letter guess? ")


index_val = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secretword):
    guess = input(f"That was not {len(secretword)} letters! Try again: ")
        
if len(guess) == len(secretword):
    if secretword == guess:
        emoji += (GREEN_BOX * len(guess))
        print(emoji + "\nWoo! You got it!")
    else:
        while index_val < len(secretword):
            if guess[index_val] == secretword[index_val]:
                emoji += GREEN_BOX
            elif guess[index_val] in secretword:
                emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
            index_val += 1
        print(emoji + "\nNot quite. Play again soon!")
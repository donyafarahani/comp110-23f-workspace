"""EX01 - Chardles - A cute step toward World."""
__author__ = "730661618"
word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
    
letter: str = input("Enter a single character:")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)
count_of_letter: int = 0
if letter == word[0]: 
    print(letter + " found at index 0")
    count_of_letter += 1
if letter == word[1]:
    print(letter + " found at index 1")
    count_of_letter += 1
if letter == word[2]:
    print(letter + " found at index 2")
    count_of_letter += 1
if letter == word[3]:
    print(letter + " found at index 3")
    count_of_letter += 1
if letter == word[4]:
    print(letter + " found at index 4")
    count_of_letter += 1
if count_of_letter == 0:
    print("No instances of " + letter + " found in " + word)
if count_of_letter == 1:
    print("1 instance of " + letter + " found in " + word)
if count_of_letter >= 2:
    print(str(count_of_letter) + " instances of " + letter + " found in " + word)

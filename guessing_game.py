"""Guessing Game
"""
SECRET_NUMBER = 9
GUESS_COUNT = 0
GUESS_LIMIT = 3
while GUESS_COUNT < GUESS_LIMIT:
    GUESS = int(input("Guess: "))
    GUESS_COUNT += 1
    if GUESS == SECRET_NUMBER:
        print("You won!")
        break
else:
    print("Sorry you failed! ")

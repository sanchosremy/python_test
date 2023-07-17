def guessing_game(secret_number, guess_count, guess_limit):
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("You won!")
        break
    else:
        print("Sorry you failed!")

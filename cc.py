import random

def guessTheNumber():
    x = random.randint(1, 100)
    print(x)

    attempts = 9

    while attempts > 0:
        playerGuess = int(input("Enter your guess: ")) #this will count as an attempt

        if playerGuess == x:
            print(f"You won! The target number was {x}")
            return

        if playerGuess < x:
            print(f"The target number is greater than your guess. {attempts} attempts left.")
        else:
            print(f"The target number is less than your guess. {attempts} attempts left.")

        attempts -= 1

    if attempts== 0:
        print(f"The correct number was {x}. You lose.")


guessTheNumber()

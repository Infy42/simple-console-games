import random

randomnum = random.randint(1,10)

def number_guesser():
    guess = input("Choose a number between 1 and 10: ")
    guessInt = int(guess)

    if guessInt < randomnum:
        print("Your number is too low! Try again: ")
        number_guesser()
    elif guessInt > randomnum:
        print("Your number is too high! Try again: ")
        number_guesser()
    elif guessInt == randomnum:
        print("Your number is correct!")
    else:
        print("Unknown Error. What the fuck did you type?!")
import random

randomrps = random.randint(1,3)
       
def rockpapperscissors():
    options = ["Rock", "Paper", "Scissors"]

    print("Choose one of the options: ")
    for index, option in enumerate(options):
        print(index + 1, " ", option)

    guess = input()
    guessInt = int(guess)

    print("You chose ", options[guessInt-1])
    print("Computer chose ", options[randomrps-1])

    if guessInt == randomrps:
        print("It's a tie!")
    elif (guessInt-1 == 0 and randomrps-1 == 1 or guessInt-1 == 1 and randomrps-1 == 2 or guessInt-1 == 2 and randomrps-1 == 0):
        print("Computer wins!")
    elif (guessInt-1 == 1 and randomrps-1 == 0 or guessInt-1 == 2 and randomrps-1 == 1 or guessInt-1 == 0 and randomrps-1 == 3):
        print("You win!")
    else:
        print("Unkown error!")
import number_guesser
import rockpaperscissors
import quiz_master


games = ["Number guesser", "Rock, Paper, Scissors", "Quiz Master"]

print("Welcome to the guessing game!")
print("Choose a guessing game: ")

try:
    for index, game in enumerate(games):
        print(index + 1, " ", game)
    choice = input()
    choiceInt = int(choice)
    print("You chose ", games[choiceInt-1],"!")

    if choiceInt == 1:
        number_guesser()
    elif choiceInt == 2:
        rockpaperscissors()
    elif choiceInt == 3:
        quiz_master()
    else:
        print("Invalid option. Bye")
except ValueError:
    print("Please use numbers from 1 to 3")
except IndexError:
    print("Please use numbers from 1 to 3")






def quiz_master():
    questions = [
        "What's the square root of 64?",
        "Where is the Eiffel Tower?",
        "Who was the first man on the moon?",
        "If you dig a 6ft hole, how deep is that hole?",
        "Ireland has physical borders with which country?",
        "How long is a week?"
    ]
    answers = [
        ["4","20","8","16"],
        ["Paris, France", "Kyoto, Japan", "Perth, Australia", "Hamburg, Germany"],
        ["Joseph Stalin", "Neil Armstrong", "Johnny Sins", "Lionel Messi"],
        ["Pi","6 feet", "Probably around 20 feet", "4 shoes"],
        ["Third Reich", "England", "Greenland", "Northern Ireland"],
        ["7 days", "2 months", "6 and a half cigarettes", "10 Spotify Ads"]
    ]
    correct_answers = [2,0,1,1,3,0]
    notifications = [
        "Wrong! :C",
        "Correct! :)"

    ]

    num_questions = len(questions)
    print("Here are 6 questions! For each correct answer you receive a point, and for each wrong answer you lose a point")

    points = 0
    for i in range(num_questions):
        print(questions[i])
        for j in range(len(answers[i])):
            print(f"{chr(65 + j)}. {answers[i][j]}")
            
        user_input = input("Your answer (A/B/C/D): ").upper()

        if user_input in ["A", "B", "C", "D"]:
            user_choice = ord(user_input) - ord("A")
            if user_choice == correct_answers[i]:
                print(notifications[1])
                points = points + 1
            else:
                print(notifications[0])
                points = points - 1
        else:
            print("Invalid input.")


    

    print("You finished with ", points, " points.")
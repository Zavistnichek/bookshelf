import random

while True:
    random_number = random.randint(1, 100)
    print("\nA new game has started. A number between 1 and 100 has been chosen.")
    while True:
        try:
            user_number = int(input("Guess the number (1-100): "))
            if user_number not in range(1, 101):
                print("Invalid input. Please enter an integer (1-100)")
            elif user_number > random_number:
                print("The number is lower than your guess.")
            elif user_number < random_number:
                print("The number is higher than your guess.")
            else:
                print("You won!")
                while True:
                    replay = input("Wanna play again? (Y/N): ")
                    if replay.lower() == "y":
                        break
                    elif replay.lower() == "n":
                        exit()
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer (1-100).")

while True:
    try:
        user_drink_number = int(input("Enter the number of the drink (1-5): "))
        if user_drink_number not in range(1, 6):
            print("Please enter a valid number (1-5).")
        else:
            drinks = {1: "water", 2: "tea", 3: "coffee", 4: "juice", 5: "milk"}
            drink = drinks[user_drink_number]
            print(f"You chose {drink}.")
            break
    except ValueError:
        print("Please enter a valid integer.")

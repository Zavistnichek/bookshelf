try:
    user_number = float(input("Enter a number: "))
    if user_number == 0:
        print(f'Number "{user_number}" is zero.')
    elif user_number > 0:
        print(f'Number "{user_number}" is positive.')
    else:
        print(f'Number "{user_number}" is negative.')
except ValueError:
    print("Please enter a valid number.")

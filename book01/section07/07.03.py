try:
    user_number_1 = float(input("Enter a first number: "))
    user_number_2 = float(input("Enter a second number: "))
    if user_number_1 == user_number_2:
        print(f'Numbers "{user_number_1}" and "{user_number_2}" are equal.')
    elif user_number_1 > user_number_2:
        print(f'Number "{user_number_1}" is greater than "{user_number_2}".')
    else:
        print(f'Number "{user_number_2}" is greater than "{user_number_1}".')
except ValueError:
    print("Please enter a valid number.")

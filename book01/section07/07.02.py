try:
    user_number = int(input("Enter a number: "))
    if user_number % 2 == 0:
        print(f'Number "{user_number}" is even.')
    else:
        print(f'Number "{user_number}" is odd.')
except ValueError:
    print("Please enter a valid integer.")

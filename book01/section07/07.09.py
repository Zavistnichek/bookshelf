try:
    user_month_number = int(input('Enter a number of month (1-12): '))
    if user_month_number not in range(1, 12 + 1):
        print('Please enter a valid number of month.')
    elif user_month_number in range(3, 5 + 1):
        print('It is spring.')
    elif user_month_number in range(6, 8 + 1):
        print('It is summer.')
    elif user_month_number in range(9, 11 + 1):
        print('It is autumn.')
    else:
        print('It is winter.')
except ValueError:
    print('Please enter a valid integer.')

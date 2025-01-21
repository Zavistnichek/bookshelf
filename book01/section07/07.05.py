try:
    user_temp = float(input(('Enter the temperature in Celsius degrees: ')))
    if user_temp < 0:
        print('It is cold outside.')
    elif user_temp > 20:
        print('It is hot outside.')
    else:
        print('It is warm outside.')
except ValueError:
    print('Please enter a valid number.')

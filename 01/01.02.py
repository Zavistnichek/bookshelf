try:
    user_num = int(input('Enter an integer: '))
    if user_num % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
except ValueError:
    print('Invalid input. Please enter an integer.')

try:
    user_number = int(input('Enter an integer to check if it is '
                            'divisible by 5 without a remainder: '))
    if user_number % 5 == 0:
        print('The given number is divisible by 5 without a remainder: '
              f'{user_number} / 5 = {int(user_number / 5)}')
    else:
        print(f'The number "{user_number}" is not '
              'divisible by 5 without a remainder.')
except ValueError:
    print('Please enter a valid integer.')

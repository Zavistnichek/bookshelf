try:
    user_number = float(input('Enter a number to square it: '))
    squared_number = user_number ** 2
    print(f'{user_number} is equal to {squared_number:.2f}')
except ValueError:
    print('Please enter a valid number.')

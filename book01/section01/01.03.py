try:
    user_num_1 = int(input('Enter the base: '))
    user_num_2 = int(input('Enter the exponent: '))
    print(f'{user_num_1} to the power of {user_num_2} = '
          f'{user_num_1**user_num_2}')
except ValueError:
    print('Error: please enter an integer.')

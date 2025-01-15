try:
    user_num_1 = int(input('Enter the first number: '))
    user_num_2 = int(input('Enter the second number: '))
    addition = user_num_1 + user_num_2
    sub = user_num_1 - user_num_2
    mul = user_num_1 * user_num_2
    print(f'The sum is: {addition}\n'
          f'The difference is: {sub}\n'
          f'The product is: {mul}')
    if user_num_2 != 0:
        print(f'The quotient is: {user_num_1 / user_num_2}')
    else:
        print('Division by zero is not possible')
except ValueError:
    print('Invalid input. Please enter valid integers.')

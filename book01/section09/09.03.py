try:
    user_dividend = float(input('Enter the dividend: '))
    user_divisor = float(input('Enter the divisor: '))
    if user_divisor == 0:
        print("Cannot divide by zero.")
    elif user_dividend % user_divisor == 0:
        print(f'{user_dividend:.0f} is divisible by '
              f'{user_divisor:.0f} without a remainder.')
        print(f'{user_dividend:.0f} / {user_divisor:.0f} = '
              f'{(user_dividend / user_divisor):.0f}')
    else:
        print(f'{user_dividend} is not divisible by '
              f'{user_divisor} without a remainder.')
        print(f'{user_dividend} / {user_divisor} = '
              f'{(user_dividend / user_divisor):.2f}')
except ValueError:
    print('Please enter a valid number.')

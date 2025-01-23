import re

user_number = input('Enter a number: ').strip()
if re.match(r'^[+-]?0(\.0+)?$', user_number):
    print(f'"{user_number}" is zero.')
elif re.match(r'^[+-]?\d+$', user_number):
    try:
        int_number = int(user_number)
        print(f'"{int_number}" is an integer.')
        if int_number % 2 == 0:
            print(f'"{int_number}" is even.')
        else:
            print(f'"{int_number}" is odd.')
        if int_number > 0:
            print(f'"{int_number}" is positive.')
        elif int_number < 0:
            print(f'"{int_number}" is negative.')
    except ValueError:
        print('Unexpected error while processing integer.')
elif re.match(r'^[+-]?\d+(\.\d+)?$', user_number):
    try:
        float_number = float(user_number)
        print(f'"{float_number}" is a floating-point number.')
        if float_number > 0:
            print(f'"{float_number}" is positive.')
        else:
            print(f'"{float_number}" is negative.')
    except ValueError:
        print('Unexpected error while processing floating-point number.')
else:
    print('The entered value is not a valid number.')

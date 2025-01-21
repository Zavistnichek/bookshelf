try:
    user_hour = int(input('Enter a current hour (0-23): '))
    if user_hour < 0 or user_hour > 23:
        print('Please enter a valid hour.')
    elif user_hour in range(5, 11 + 1):
        print('It is morning.')
    elif user_hour in range(12, 17 + 1):
        print('It is afternoon.')
    elif user_hour in range(18, 22 + 1):
        print('It is evening.')
    else:
        print('It is night.')
except ValueError:
    print('Please enter a valid hour.')

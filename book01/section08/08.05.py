while True:
    try:
        days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }
        day_input = int(input('Enter the day of the week number (1-7): '))
        if 1 <= day_input <= 7:
            print(f'It is {days[day_input]}.')
            break
        else:
            print('Please enter a number between 1 and 7.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

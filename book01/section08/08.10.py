months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
days_in_month = {
    31: ['January', 'March', 'May', 'July', 'August', 'October', 'December'],
    30: ['April', 'June', 'September', 'November'],
    28: ['February'],
    29: ['February']
}
user_date = int(input('Enter the number of the day: '))
if user_date <= 0:
    print('A date must be a positive integer and not zero.')
elif user_date > 31:
    print(f'There is no day {user_date} in any month.')
else:
    possible_months = [(month for days, months in days_in_month.items()
                        if user_date <= days for month in months)]
    print(f'The entered date occurs in the months: '
          f'{", ".join(list(possible_months))}')

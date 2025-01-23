try:
    user_age = int(input('Enter your age to get a ticket: ')).strip()
    if user_age < 0:
        print('Age cannot be negative.')
    elif user_age < 5:
        print('Your ticket is free (up to 5 years old).')
    elif user_age < 13:
        print('Your ticket costs $5 (children aged 5-12).')
    elif user_age < 60:
        print('Your ticket costs $10 (adults aged 13-59).')
    else:
        print('Your ticket is free (for seniors 60 and older).')
except ValueError:
    print('Please enter a valid integer.')

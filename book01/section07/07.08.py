password = '12345'
attempts = 3

while attempts > 0:
    user_input = input('Enter a password: ')
    if user_input == password:
        print('The password is correct. Access granted.')
        break
    else:
        attempts -= 1
        print(f'Incorrect password. {attempts} attempts left.')
        if attempts == 0:
            print('Access denied. Too many failed attempts.')

user_list = input('Enter list elements separated by spaces: ').split()
user_check = input('Enter an element to check: ')

if user_check in user_list:
    print(True)
else:
    print(False)

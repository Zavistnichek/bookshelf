user_input = input('Введите строку: ')

user_old_char = input('Символ для замены: ')
if len(user_old_char) != 1:
    print('Ошибка: символ для замены должен быть длиной в один символ.')
else:
    user_new_char = input('На что заменить: ')
    if len(user_new_char) != 1:
        print('Ошибка: символ-замена должен быть длиной в один символ.')
    else:
        print(user_input.replace(user_old_char, user_new_char))



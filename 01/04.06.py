user_list = input('Введите элементы списка через пробел: ').split()
user_check = input('Введите элемент для проверки: ')

if user_check in user_list:
    print(True)
else:
    print(False)

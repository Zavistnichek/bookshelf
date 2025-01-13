user_string = input('Введите строку: ')
user_index_1 = int(input('Введите первый индекс: '))
user_index_2 = int(input('Введите второй индекс: '))

if user_index_1 < 0 or user_index_2 > len(user_string) or user_index_1 > user_index_2:
    print('Некорректные индексы')
else:
    result = user_string[user_index_1:user_index_2]
    print('Извлеченная подстрока:', result)

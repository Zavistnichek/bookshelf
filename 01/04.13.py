user_input = input('Введите список элементов через пробел: ')
user_elem = input('Введите элемент из списка: ')

list_of_elements = user_input.split()

if len(user_elem.split()) != 1:
    print('Пожалуйста, введите один элемент.')
elif user_elem not in list_of_elements:
    print('Данный элемент отсутствует в списке.')
else:
        count = list_of_elements.count(user_elem)
        print(f'Элемент {user_elem} встречается в списке {count} раз')

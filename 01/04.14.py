user_input = input('Введите список элементов через пробел: ').strip()
user_element = input('Введите элемент для удаления его первого вхождения в список: ').strip()

list_of_elements = user_input.split()

try:
    list_of_elements.remove(user_element)
    print('Обновлённый список: ', list_of_elements)
except:
    print(f'Элемент "{user_element}" не найден в списке.')

input_1 = input('Введите элементы первого списка через пробел: ')
input_2 = input('Введите элементы второго списка через пробел: ')

list_1, list_2 = input_1.split(), input_2.split()

result = list_1 + list_2

print(result)

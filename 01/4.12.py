input_1 = input('Введите первый список элементов через пробел: ')
input_2 = input('Введите второй список элементов через пробел: ')

list_1, list_2 = input_1.split(), input_2.split()
result = list_1+list_2
result.sort()

print(f'Отсортированный список: {result}')

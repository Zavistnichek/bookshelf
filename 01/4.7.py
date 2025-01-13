user_input = input('Введите список элементов через пробел: ')

list_of_elements = user_input.split()
reversed_list = list_of_elements[::-1]

print(reversed_list)

user_list = input('Введите список элементов через пробел: ')
user_n = int(input('Введите число n: '))

list_of_elements = user_list.split()

n = user_n % len(list_of_elements)
result = list_of_elements[-n:] + list_of_elements[:-n]

print(result)

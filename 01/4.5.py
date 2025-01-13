user_input = input('Введите числа через пробел: ')

list_of_numbers = user_input.split()
unique_numbers = set(list_of_numbers)

print(unique_numbers)
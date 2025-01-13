user_numbers = input('Введите список чисел через пробел: ')

numbers_list = list(map(int, user_numbers.split()))

even_numbers = [x for x in numbers_list if x % 2 == 0]
odd_numbers = [x for x in numbers_list if x % 2 != 0]

print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")

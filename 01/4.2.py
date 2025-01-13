import math

user_input = input('Введите числа через пробел: ')

list_of_numbers = user_input.split()

def is_valid_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

if not all(is_valid_number(item) for item in list_of_numbers):
    print('Пожалуйста, введите только числа!')
else:
        numbers = [int(number) for number in list_of_numbers]
        result = math.prod(numbers)
        print('Произведение чисел:', result)

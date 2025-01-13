user_input = input('Введите список элементов через пробел: ')

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
    even_numbers = [int(x) for x in list_of_numbers if int(x) % 2 == 0]
    print('Чётные числа:', even_numbers)

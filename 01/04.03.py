user_input = input('Введите числа через пробел: ')

list_of_numbers = user_input.split()


def is_valid_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


if not list_of_numbers or not all(is_valid_number(item) for item in list_of_numbers):
    print('Пожалуйста, введите только числа!')
else:
    numbers = [int(number) for number in list_of_numbers]
    max_number = max(numbers)
    min_number = min(numbers)
    print(f'Минимальное число: {min_number}\nМаксимальное число: {max_number}')

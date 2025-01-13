user_input = input('Введите числа через пробел: ')

list_of_numbers = user_input.split()


def is_valid_number(item):
    try:
        float(item)
        return True
    except ValueError:
        return False


if not list_of_numbers or not all(is_valid_number(item) for item in list_of_numbers):
    print('Пожалуйста, введите только числа!')
else:
    numbers = [float(number) for number in list_of_numbers]
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        print(f'Среднее значение: {average:.2f}')
    else:
        print('Ошибка: нет чисел для вычисления среднего значения.')

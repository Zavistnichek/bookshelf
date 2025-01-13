user_input = input('Введите числа через пробел: ')

list_of_numbers = user_input.split()

if not all(item.isdigit() for item in list_of_numbers):
    print('Пожалуйста, введите только числа!')
else:
    numbers = [int(number) for number in list_of_numbers]
    result = sum(numbers)
    print('Сумма чисел:', result)

user_num = int(input('Введите число: '))
sum_of_digits = sum(map(int, str(user_num)))

print(f'Сумма цифр числа {user_num} = {sum_of_digits}')

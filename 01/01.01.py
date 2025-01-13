user_num_1 = int(input('Введите первое число: '))
user_num_2 = int(input('Введите второе число: '))

addition = user_num_1 + user_num_2
sub = user_num_1 - user_num_2
mul = user_num_1 * user_num_2

print(f'Сумма равна: {addition}\n'
      f'Разность равна: {sub}\n'
      f'Произведение равно: {mul}')

if user_num_2 != 0:
    print(f'Частное равно: {user_num_1 / user_num_2}')
else:
    print('Деление на ноль невозможно')

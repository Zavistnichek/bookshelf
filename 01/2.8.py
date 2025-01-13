n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))

if n1 == n2:
    print('Числа равны')
else:
    difference = abs(n1 - n2)
    print(f'Числа различаются на {difference:.3f}')
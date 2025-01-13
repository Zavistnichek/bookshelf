count = int(input('Введите количество чисел для суммирования: '))
l = []

if count == 0:
    print('Ошибка ввода. Количество чисел должно быть больше нуля.')
else:
    for n in range(count):
        number = float(input(f'Введите {n+1} число: '))
        l.append(number)

    total = sum(l)
    print(f'Сумма чисел: {total}')

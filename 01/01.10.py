num = int(input('Введите число: '))

reversed_iterator = reversed(str(num))
reversed_str = ''.join(reversed_iterator)
reversed_num = int(reversed_str)

print(f'Число {num} наоборот: {reversed_num}')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def gcd(a, b):
    print(f'Начинаем вычисление НОД для {a} и {b}')
    while b != 0:
        print(f'Текущие значения: a = {a}, b = {b}')
        a, b = b, a % b
        print(f'После операции: a = {a}, b = {b}')
    return a

print(f'НОД чисел {a} и {b} равен {gcd(a, b)}')

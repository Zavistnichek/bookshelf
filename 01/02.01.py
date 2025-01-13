num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))

print(f'{num1} + {num2} = {num1 + num2:.4g}')
print(f'{num1} - {num2} = {num1 - num2:.4g}')
print(f'{num1} * {num2} = {num1 * num2:.4g}')

try:
    print(f'{num1} / {num2} = {num1 / num2:.4g}')
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")

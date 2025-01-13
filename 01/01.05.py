n = int(input('Введите число: '))
f = 1

for i in range(1, n + 1):
    f *= i

print(f"Факториал числа {n} равен {f}")

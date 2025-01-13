import math

r = float(input('Радиус основания цилиндра: '))
h = float(input('Высота цилиндра: '))
V = r**2 * h * math.pi

print(f'Объём цилиндра: {V:.2f}')
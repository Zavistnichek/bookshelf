import math, cmath

n = float(input('Введите число: '))
if n >= 0:
    sq_n = math.sqrt(n)
else:
    sq_n = cmath.sqrt(n)

if isinstance(sq_n, complex):
    print(f'{sq_n.real:.2f} + {sq_n.imag:.2f}j')
else:
    print(f'{sq_n:.2f}')

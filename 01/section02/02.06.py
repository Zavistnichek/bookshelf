import math
import cmath

try:
    n = float(input('Enter a number: '))
    if n >= 0:
        sq_n = math.sqrt(n)
    else:
        sq_n = cmath.sqrt(n)
except ValueError:
    print("Error: input is not a number.")
    exit(1)

if isinstance(sq_n, complex):
    print(f'{sq_n.real:.2f} + {sq_n.imag:.2f}j')
else:
    print(f'{sq_n:.2f}')

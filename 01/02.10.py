import math

try:
    r = float(input('Radius of the cylinder base: '))
    h = float(input('Height of the cylinder: '))
    V = r**2 * h * math.pi
    print(f'Volume of the cylinder: {V:.2f}')
except ValueError:
    print("Please enter a numerical value for the radius and height.")

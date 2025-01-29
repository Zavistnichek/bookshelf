import math

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
        area = radius**2 * math.pi
    print(f"Area of the circle = {area:.4g}")
except ValueError as e:
    print(f"Invalid input: {e}")

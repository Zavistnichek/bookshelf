def solve_quadratic(a, b, c):
    if a == 0:
        return (
            "This is not a quadratic equation. "
            "The coefficient 'a' cannot be zero."
        )
    D = b**2 - 4*a*c
    if D > 0:
        sqrt_D = D ** 0.5
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        return f"Discriminant: {D}, two roots: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Discriminant: {D}, one root: x = {x}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(D) ** 0.5) / (2 * a)
        return (
            f'Discriminant: {D}, '
            f'complex roots: x1 = {real_part} + {imaginary_part}j, '
            f'x2 = {real_part} - {imaginary_part}j'
        )


try:
    a = int(input('Enter coefficient a: '))
    b = int(input('Enter coefficient b: '))
    c = int(input('Enter coefficient c: '))
    print(solve_quadratic(a, b, c))
except ValueError:
    print("Please enter integers for the coefficients.")

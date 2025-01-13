def solve_quadratic(a, b, c):
    if a == 0:
        return "Это не квадратное уравнение. Коэффициент 'a' не может быть равен 0."
    
    D = b**2 - 4*a*c
    
    if D > 0:
        sqrt_D = D ** 0.5
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        return f"Дискриминант: {D}, два корня: x1 = {x1}, x2 = {x2}"
    
    elif D == 0:
        x = -b / (2 * a)
        return f"Дискриминант: {D}, один корень: x = {x}"
    
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(D) ** 0.5) / (2 * a)
        return f"Дискриминант: {D}, комплексные корни: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"

a = int(input('Ввведите коэффициент a: '))
b = int(input('Ввведите коэффициент b: '))
c = int(input('Ввведите коэффициент c: '))
print(solve_quadratic(a, b, c))

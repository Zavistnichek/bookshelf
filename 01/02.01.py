try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
except ValueError:
    print("Error: Non-numeric value entered!")
else:
    print(f'{num1} + {num2} = {num1 + num2:.4g}')
    print(f'{num1} - {num2} = {num1 - num2:.4g}')
    print(f'{num1} * {num2} = {num1 * num2:.4g}')
    try:
        print(f'{num1} / {num2} = {num1 / num2:.4g}')
    except ZeroDivisionError:
        print("Error: Division by zero!")

try:
    n = float(input('Enter the number to be rounded: '))
    print(f'{n:.2f}')
except ValueError:
    print('Error: non-numeric value entered')

try:
    n1 = float(input('Enter the first number: '))
    n2 = float(input('Enter the second number: '))

    if n1 == n2:
        print('The numbers are equal')
    else:
        difference = abs(n1 - n2)
        print(f'The numbers differ by {difference:.3f}')
except ValueError:
    print('Please enter a numeric value.')

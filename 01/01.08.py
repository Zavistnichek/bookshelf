try:
    n = int(input('Enter a positive integer: '))
    if n <= 1:
        print(f'The number {n} is neither prime nor composite')
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'The number {n} is prime')
        else:
            print(f'The number {n} is composite')
except ValueError:
    print('Invalid input. Please enter a positive integer.')

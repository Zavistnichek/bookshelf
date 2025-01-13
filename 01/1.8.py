n = int(input('Введите число: '))

if n <= 1:
    print(f'Число {n} не является простым и не является составным')
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'Число {n} простое')
    else:
        print(f'Число {n} составное')

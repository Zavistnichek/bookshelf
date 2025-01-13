num = int(input("Введите число: "))
divisors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Делители числа {num}: {divisors}")

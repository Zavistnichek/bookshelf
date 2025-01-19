try:
    num = int(input("Enter a number: "))
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    print(f"Divisors of the number {num}: {divisors}")
except ValueError:
    print("Please enter a valid integer.")

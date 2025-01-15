try:
    n = int(input('Enter a number: '))
    if n < 0:
        print("Please enter a positive number")
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        print(f"The factorial of {n} is {f}")
except ValueError:
    print("Please enter an integer")

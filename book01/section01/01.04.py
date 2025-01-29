try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid integers.")
    exit(1)


def gcd(a, b):
    print(f"Starting GCD calculation for {a} and {b}")
    while b != 0:
        print(f"Current values: a = {a}, b = {b}")
        a, b = b, a % b
        print(f"After operation: a = {a}, b = {b}")
    return a


print(f"The GCD of {a} and {b} is {gcd(a, b)}")

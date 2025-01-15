try:
    num = int(input("Enter a number: "))
    print(f"Binary system: {bin(num)[2:]}")
    print(f"Octal system: {oct(num)[2:]}")
    print(f"Hexadecimal system: {hex(num)[2:]}")
except ValueError:
    print("Please enter a valid integer number")

try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    n3 = float(input("Enter the third number: "))
    n4 = float(input("Enter the fourth number: "))
    n5 = float(input("Enter the fifth number: "))
    average = (n1 + n2 + n3 + n4 + n5) / 5
    print(f"The arithmetic mean of the numbers = {average:.2f}")
except ValueError:
    print("Please enter valid numbers.")

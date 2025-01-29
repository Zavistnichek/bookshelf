try:
    num = int(input("Enter a number: "))
    reversed_iterator = reversed(str(num))
    reversed_str = "".join(reversed_iterator)
    reversed_num = int(reversed_str)
    print(f"The number {num} reversed is: {reversed_num}")
except ValueError:
    print("Please enter a valid integer number")

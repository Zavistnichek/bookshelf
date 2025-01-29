try:
    count = int(input("Enter the number of numbers to sum: "))
    if count <= 0:
        raise ValueError
except ValueError:
    print("Input error. The number of numbers must be a positive integer.")
else:
    list_of_numbers = []
    for n in range(count):
        number = float(input(f"Enter number {n+1}: "))
        list_of_numbers.append(number)
    total = sum(list_of_numbers)
    print(f"The sum of the numbers is: {total}")

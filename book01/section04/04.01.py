user_input = input("Enter numbers separated by spaces: ").strip()
list_of_numbers = user_input.split()

if not all(item.isdigit() for item in list_of_numbers):
    print("Please enter only numbers!")
else:
    numbers = [int(number) for number in list_of_numbers]
    result = sum(numbers)
    print("Sum of numbers:", result)

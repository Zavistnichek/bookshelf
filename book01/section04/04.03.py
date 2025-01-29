user_input = input("Enter numbers separated by spaces: ")
list_of_numbers = user_input.split()


def is_valid_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


if not list_of_numbers or not all(is_valid_number(item) for item in list_of_numbers):
    print("Please enter only numbers!")
else:
    numbers = [int(number) for number in list_of_numbers]
    max_number = max(numbers)
    min_number = min(numbers)
    print(f"Minimum number: {min_number}\n" f"Maximum number: {max_number}")

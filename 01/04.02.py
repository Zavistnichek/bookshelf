import math

user_input = input('Enter numbers separated by spaces: ')
list_of_numbers = user_input.split()


def is_valid_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


if not all(is_valid_number(item) for item in list_of_numbers):
    print('Please enter only numbers!')
else:
    numbers = [int(number) for number in list_of_numbers]
    result = math.prod(numbers)
    print('Product of numbers:', result)

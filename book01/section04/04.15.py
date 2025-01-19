user_input = input('Enter a list of elements separated by spaces: ')
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
    even_numbers = [int(x) for x in list_of_numbers if int(x) % 2 == 0]
    print('Even numbers:', even_numbers)

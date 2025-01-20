print('Enter two lists of the same length. ')
first_input = input(
    'Enter the first list of the elements separated by spaces (keys): '
    ).strip()
second_input = input(
    'Enter the second list of the elements separated by spaces (values): '
    ).strip()

first_list = list(first_input.split())
second_list = list(second_input.split())
if len(first_list) != len(second_list):
    print('Please enter dictionaries of the same length.')
else:
    dictionary = dict(zip(first_list, second_list))
    print(dictionary)

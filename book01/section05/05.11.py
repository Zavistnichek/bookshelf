from tuple_parser import parse_element

user_input = input('Enter the numbers separated by commas: ')
try:
    user_tuple = tuple(parse_element(e) for e in user_input.split(','))
    print(min(user_tuple))
    print(max(user_tuple))
except ValueError:
    print('Please enter only numbers!')

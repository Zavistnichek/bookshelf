from tuple_parser import parse_element

user_input = input('Enter the elements of the tuple separeted by commas: ')
user_tuple = tuple(parse_element(e) for e in user_input.split(','))
print(len(user_tuple))

from tuple_parser import parse_element

user_input = input('Enter the elements of the tuple separated by commas: ')
user_tuple = tuple(parse_element(e) for e in user_input.split(','))
for element in user_tuple:
    print(element)

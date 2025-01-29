from tuple_parser import parse_element

user_input = input("Enter tuple elements separated by commas: ")
user_element = input("Enter element to search for: ")
user_tuple = tuple(parse_element(e) for e in user_input.split(","))
search_element = parse_element(user_element)

if search_element in user_tuple:
    print("True")
else:
    print("False")

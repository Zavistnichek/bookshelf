from tuple_parser import parse_element

user_input = input("Enter the elements of the tuple separated by commas: ").strip()
if not user_input:
    print("No input provided!")
else:
    user_tuple = tuple(parse_element(e) for e in user_input.split(","))
    print("First element of the tuple:", user_tuple[0])
    print("Last element of the tuple:", user_tuple[-1])

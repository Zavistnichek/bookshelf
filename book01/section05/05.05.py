from tuple_parser import parse_element

user_input = input("Enter the elements of the tuple separated by commas: ")

try:
    user_tuple = tuple(parse_element(e) for e in user_input.split(","))
    union_tuple = user_tuple * 3
    print("This tuple replicated three times:", union_tuple)
except Exception as e:
    print(f"Error: {e}. Please check the input format.")

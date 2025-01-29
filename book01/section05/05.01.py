from tuple_parser import parse_element

try:
    user_input = input("Enter the elements of the tuple separated by commas: ").strip()
    if not user_input:
        print("No elements provided!")
    else:
        user_tuple = tuple(parse_element(e) for e in user_input.split(","))
        print("Created tuple:", user_tuple)
except ValueError as ve:
    print(f"Value error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

from tuple_parser import parse_element

input_1 = input("Enter the elements of the first tuple separated by commas: ")
input_2 = input("Enter the elements of the second tuple separated by commas: ")

try:
    tuple_1 = tuple(parse_element(e) for e in input_1.split(","))
    tuple_2 = tuple(parse_element(e) for e in input_2.split(","))
except Exception as e:
    print(f"Error parsing input: {e}")
    exit()

union_tuple = tuple_1 + tuple_2
print("Union tuple:", union_tuple)

from tuple_parser import parse_element

user_input = input('Enter the elements of the tuple separated by commas: ')

try:
    user_index_1 = int(input('Enter the first index for slicing the tuple: '))
    user_index_2 = int(input('Enter the second index for slicing the tuple: '))
except ValueError:
    print("Please enter valid integer indices.")
    exit()

user_tuple = tuple(parse_element(e) for e in user_input.split(','))
tuple_length = len(user_tuple)

if (user_index_1 < 0 or
        user_index_2 > tuple_length or
        user_index_1 > user_index_2):
    print(f"Invalid indices. Tuple length is {tuple_length}.")
else:
    sliced = user_tuple[user_index_1:user_index_2]
    print('Sliced tuple:', sliced)

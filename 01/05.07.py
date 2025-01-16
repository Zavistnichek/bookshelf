original_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", original_tuple)

list_from_tuple = list(original_tuple)
print("List from tuple:", list_from_tuple)

list_from_tuple[2] = 10
list_from_tuple.append(6)

modified_tuple = tuple(list_from_tuple)
print("Restored tuple:", modified_tuple)

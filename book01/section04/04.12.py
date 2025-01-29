input_1 = input("Enter the first list of elements separated by spaces: ")
input_2 = input("Enter the second list of elements separated by spaces: ")
list_1, list_2 = input_1.split(), input_2.split()
result = list_1 + list_2
result.sort()
print(f"Sorted list: {result}")

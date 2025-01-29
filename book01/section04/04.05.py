user_input = input("Enter numbers separated by spaces: ")
list_of_numbers = map(int, user_input.split())
unique_numbers = set(list_of_numbers)
print(unique_numbers)

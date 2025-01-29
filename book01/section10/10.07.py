strings = ["string 1", "string 2", "string 3", "string 4"]
user_input = input("Enter a string: ")
found = False

for index, string in enumerate(strings):
    if string == user_input:
        print(f'"{user_input}" is in the list at index {index}.')
        found = True
        break

if not found:
    print(f'"{user_input}" is not in the list.')

user_input = input("Enter a list of elements separated by spaces: ").strip()
user_element = input(
    "Enter an element to remove its first occurrence from the list: "
).strip()
list_of_elements = user_input.split()

try:
    list_of_elements.remove(user_element)
    print("Updated list: ", list_of_elements)
except ValueError:
    print(f'Element "{user_element}" not found in the list.')

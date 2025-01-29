user_input = input("Enter a list of elements separated by spaces: ")
user_elem = input("Enter an element from the list: ")
list_of_elements = user_input.split()

if len(user_elem.split()) != 1:
    print("Please enter one element.")
elif user_elem not in list_of_elements:
    print("This element is not in the list.")
else:
    count = list_of_elements.count(user_elem)
    print(f"The element {user_elem} appears in the list {count} times")

from tuple_parser import parse_element

user_input = input("Enter the elements of the tuple separated by commas: ")
user_tuple = tuple(parse_element(e) for e in user_input.split(","))
print(f"Original tuple: {user_tuple}")

try:
    index = int(input("Enter the index of the element you want to change: "))
    new_value = input("Enter the new value for this element: ")
    user_tuple[index] = new_value
except TypeError as e:
    print(f"Error: {e}")
    proceed = (
        input(
            "Do you wish to proceed and convert a tuple"
            "into a list to change an element? (yes/no): "
        )
        .strip()
        .lower()
    )
    if proceed == "yes":
        user_list = list(user_tuple)
        try:
            user_list[index] = parse_element(new_value)
            user_tuple = tuple(user_list)
            print(f"Updated tuple: {user_tuple}")
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No changes made to the tuple.")
except IndexError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

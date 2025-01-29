my_dict = {"name": "Alice", "age": 25, "city": "New York"}

key_to_remove = input("Enter the key to remove: ")

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The element with the key '{key_to_remove}' has been removed.")
else:
    print(f"The key '{key_to_remove}' was not found in the dictionary.")

print("Updated dictionary:", my_dict)

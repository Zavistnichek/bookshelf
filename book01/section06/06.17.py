my_dict = {"name": "Alice", "age": 25}

name = my_dict.setdefault("name", "Unknown")
print(f"Value of 'name': {name}")
city = my_dict.setdefault("city", "New York")
print(f"Value of 'city': {city}")

print("Updated dictionary:", my_dict)

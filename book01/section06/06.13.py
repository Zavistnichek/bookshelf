my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict.keys())}
print(sorted_dict)

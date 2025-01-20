first_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

second_dict = {
    'fruit': 'apple',
    'weight': 200,
    'color': 'red',
}

combined_dict = {**first_dict, **second_dict}
print('Combined dictionary:', combined_dict)

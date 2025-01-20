nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 25,
        'city': 'New York'
    },
    'person2': {
        'name': 'Bob',
        'age': 30,
        'city': 'San Francisco'
    },
    'person3': {
        'name': 'Charlie',
        'age': 35,
        'city': 'Los Angeles'
    }
}

print('Nested Dictionary:')
for key, value in nested_dict.items():
    print(f'{key}: {value}')

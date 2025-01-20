dictionary = {
    'apple': 5,
    'banana': 3,
    'cherry': 7
}

key = input('Enter the key to search for the value: ')

if key in dictionary:
    print(f'The value for the key "{key}": {dictionary[key]}')
else:
    print(f'The key "{key}" was not found in the dictionary.')

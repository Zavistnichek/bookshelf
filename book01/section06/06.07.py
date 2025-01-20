my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

key_to_check = input('Enter the key ti check: ')
key_exists = key_to_check in my_dict
print('Check result:', key_exists)

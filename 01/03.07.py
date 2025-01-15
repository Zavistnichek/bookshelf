user_input = input('Enter a string: ')
result = ''.join(
    [char.lower() if char.isupper() else char.upper() for char in user_input]
)
print(result)

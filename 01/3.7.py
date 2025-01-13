user_input = input('Введите строку: ')

result = ''.join([char.lower() if char.isupper() else char.upper() for char in user_input])
print(result)
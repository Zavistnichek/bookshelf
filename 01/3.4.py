import string

user_input = input('Введите строку: ')
lowered = user_input.lower()
no_punctuation = ''.join(char for char in lowered if char not in string.punctuation)
cleared_input = ''.join(no_punctuation.split())
reversed_string = cleared_input[::-1]

if cleared_input == reversed_string:
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')

user_input = input("Enter a string: ")

while True:
    user_old_char = input("Character to replace: ")
    if len(user_old_char) != 1:
        print("Error: the character to replace must be one character long.")
    else:
        break

while True:
    user_new_char = input("Replace with: ")
    if len(user_new_char) != 1:
        print("Error: the replacement character must be one character long.")
    else:
        break

print(user_input.replace(user_old_char, user_new_char))

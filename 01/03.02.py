user_input = input('Enter a string: ')
if not user_input:
    print("Error: empty string entered.")
else:
    char_count = {}
    for char in user_input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        print(f"'{char}': {count}")

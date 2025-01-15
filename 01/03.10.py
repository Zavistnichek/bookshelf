user_input = input("Enter a string: ")

if user_input.strip():
    formatted_string = user_input.title()
    print("Formatted string:", formatted_string)
else:
    print("Empty string entered.")

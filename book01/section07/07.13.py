user_string = input("Enter a string: ").strip()
if not user_string or user_string.isspace():
    print("You entered an empty string.")
elif len(user_string) > 10:
    print("This string is longer than 10 symbols.")
elif len(user_string) == 10:
    print("This string is exactly 10 symbols long.")
else:
    print("This string is shorter than 10 symbols.")

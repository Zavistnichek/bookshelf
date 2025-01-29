import string

user_input = input("Enter a string: ")

if not user_input.strip():
    print("An empty string is not a palindrome")
else:
    lowered = user_input.lower()
    no_punctuation = "".join(char for char in lowered if char not in string.punctuation)
    cleared_input = "".join(no_punctuation.split())
    reversed_string = cleared_input[::-1]

    if cleared_input == reversed_string:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

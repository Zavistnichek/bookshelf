import re

user_input = input("Enter a string: ")
result = re.sub(r"\s+", "", user_input)
print(f"String without spaces: {result}")

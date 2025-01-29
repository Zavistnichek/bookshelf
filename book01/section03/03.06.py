user_string = input("Enter a string: ")
user_index_1 = int(input("Enter the first index: "))
user_index_2 = int(input("Enter the second index: "))

if user_index_1 < 0 or user_index_2 >= len(user_string) or user_index_1 > user_index_2:
    print("Invalid indices")
else:
    result = user_string[user_index_1:user_index_2]
    print("Extracted substring:", result)

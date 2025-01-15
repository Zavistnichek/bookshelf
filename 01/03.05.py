def count_words(string):
    words = string.split()
    return len(words)


user_input = input("Enter a string: ")
if not user_input.strip():
    print("Error: an empty string was entered.")
else:
    word_count = count_words(user_input)
    print(f"Number of words in the string: {word_count}")

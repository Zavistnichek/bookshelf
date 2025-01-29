def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


input_string = "Python is a high-level programming language"
result = count_words(input_string)
print(f"Number of words: {result}")

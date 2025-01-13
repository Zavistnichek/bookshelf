def count_words(string):
    words = string.split()
    return len(words)

user_input = input("Введите строку: ")

word_count = count_words(user_input)
print(f"Количество слов в строке: {word_count}")

def filter_strings_by_length(strings, min_length):
    filtered_strings = []
    for string in strings:
        if len(string) > min_length:
            filtered_strings.append(string)
    return filtered_strings


original_list = ["apple", "banana", "kiwi", "orange", "pear"]
min_length = 5
result_list = filter_strings_by_length(original_list, min_length)

print(f"Original list: {original_list}")
print(f"Strings longer than {min_length}: {result_list}")

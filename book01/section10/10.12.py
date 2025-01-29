def find_substrings(s, length):
    if length > len(s):
        return []

    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i : i + length]
        substrings.append(substring)

    return substrings


input_string = "abcdefg"
substring_length = 3
result = find_substrings(input_string, substring_length)

print(f"All substrings of length {substring_length}: {result}")

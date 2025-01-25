input_string = input("Enter a string: ")
if not input_string:
    print("The string is empty.")
else:
    vowels = "aeiouAEIOUаеёиоуэюяАЕЁИОУЭЮЯ"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1

    print(f'The number of vowels in the string is: {vowel_count}')

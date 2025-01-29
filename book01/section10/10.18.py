def double_numbers(numbers):
    doubled = []
    for number in numbers:
        doubled.append(number * 2)
    return doubled


original_list = [1, 2, 3, 4, 5]
result_list = double_numbers(original_list)

print(f"Original list: {original_list}")
print(f"Doubled list: {result_list}")

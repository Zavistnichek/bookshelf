numbers = [3, 12, 5, 8, 7, 20, 15]
max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print(f"The maximum value in the list is: {max_value}")

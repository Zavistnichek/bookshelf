def generate_range(start, end):
    numbers = []
    for number in range(start, end + 1):
        numbers.append(number)
    return numbers


start_value = 3
end_value = 10
result_list = generate_range(start_value, end_value)

print(f"Numbers in the range from {start_value} to {end_value}: {result_list}")

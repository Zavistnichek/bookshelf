user_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, user_numbers.split()))
even_numbers = [x for x in numbers_list if x % 2 == 0]
odd_numbers = [x for x in numbers_list if x % 2 != 0]
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")

user_numbers = input("Enter a list of numbers separated by spaces: ")
user_sort = input("How to sort? (1 - ascending, 2 - descending): ")

while user_sort not in ["1", "2"]:
    print("Error: enter 1 or 2.")
    user_sort = input("How to sort? (1 - ascending, 2 - descending): ")

numbers_list = list(map(int, user_numbers.split()))

if user_sort == "1":
    numbers_list.sort()
    print(f"Ascending: {numbers_list}")
else:
    numbers_list.sort(reverse=True)
    print(f"Descending: {numbers_list}")

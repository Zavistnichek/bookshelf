try:
    user_num = int(input("Enter a number: "))
    sum_of_digits = sum(map(int, str(user_num)))
    print(f"The sum of the digits of the number {user_num} = {sum_of_digits}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

try:
    number = int(input("Enter a number: "))
    original = str(number)
    reversed_number = ""
    for char in original:
        reversed_number = char + reversed_number
    if original == reversed_number:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

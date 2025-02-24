total = 0

while True:
    try:
        num = int(input("Enter a number (0 to get the sum): "))
        if num == 0:
            print("Total sum:", total)
            break
        total += num
    except ValueError:
        print("Invalid input. Please enter an integer.")

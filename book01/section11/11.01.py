while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

i = 1
while i <= num:
    print(i)
    i += 1

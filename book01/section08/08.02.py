while True:
    try:
        user_age = int(input("Enter the person's age: "))
        if user_age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif user_age <= 2:
            print("The person is a toddler (0-2 years old).")
        elif user_age <= 12:
            print("The person is a child (3-12 years old).")
        elif user_age <= 19:
            print("The person is a teenager (13-19 years old).")
        elif user_age <= 64:
            print("The person is an adult (20-64 years old).")
        else:
            print("The person is an elder (65+ years old).")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        print("A human age cannot be a negative integer.")
    elif user_age > 122:
        print("I guess you are lying.")
    elif user_age < 4:
        print("Are you sure you are even able to read and type?")
    elif user_age < 18:
        print("You are a minor. Access denied.")
    else:
        print("You are an adult. Access granted.")
except ValueError:
    print("Please enter a valid integer.")

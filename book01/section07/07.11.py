try:
    user_year = int(input("Enter a number of year: "))
    if user_year <= 0:
        print("Please enter a valid positive year.")
    elif (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
        print("The year is leap.")
    else:
        print("The year is not leap.")
except ValueError:
    print("Please enter a valid integer.")

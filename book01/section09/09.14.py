day_of_week = input("Enter a day of the week: ").strip().lower()

if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print(f"{day_of_week.capitalize()} is a working day.")
elif day_of_week in ["sunday", "saturady"]:
    print(f"{day_of_week.capitalize()} is a weekend.")
else:
    print("Please enter a valid day of week.")

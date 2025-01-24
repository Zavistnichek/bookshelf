day_of_week = input("Enter a day of the week: ").strip().lower()

# Check if the day is a working day
if day_of_week in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print(f"{day_of_week.capitalize()} is a working day.")
else:
    print(f"{day_of_week.capitalize()} is a weekend.")

try:
    C = float(input("Enter the temperature in Celsius: "))
    F = C * (9 / 5) + 32
    print(f"{C} degrees Celsius in Fahrenheit = {F:.2f}")
except ValueError:
    print("Please enter a numeric value.")

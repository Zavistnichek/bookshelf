try:
    user_dollar = float(input("Enter the amount in dollars: "))
    euro = 0.85
    dollar_in_euro = user_dollar * euro
    print(f"{user_dollar} dollars in euros = {dollar_in_euro:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

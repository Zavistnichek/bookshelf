try:
    user_price = float(input("Enter the price of the product: "))
    user_discount = float(input("Enter the discount percentage (0-100): "))
    if user_price < 0 or user_discount < 0 or user_discount > 100:
        print("Please enter valid values.")
    else:
        discount_amount = user_price * user_discount / 100
        final_price = user_price - discount_amount
        print(f"Discount amount: {discount_amount:.2f}")
        print(f"Final price: {final_price:.2f}")
except ValueError:
    print("Please enter a valid number.")

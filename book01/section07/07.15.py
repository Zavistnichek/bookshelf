try:
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))
    if weight <= 0 or height_cm <= 0:
        print("Please enter positive values for weight and height.")
    else:
        height_m = height_cm / 100
        bmi = weight / (height_m**2)
        print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")

        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
except ValueError:
    print("Please enter valid numbers for weight and height.")

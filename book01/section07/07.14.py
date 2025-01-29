try:
    user_score = float(input("Enter your score (0-100): "))
    if user_score < 0 or user_score > 100:
        print("Please enter a valid score between 0 and 100.")
    elif user_score >= 90:
        print("Your grade is A.")
    elif user_score >= 80:
        print("Your grade is B.")
    elif user_score >= 70:
        print("Your grade is C.")
    elif user_score >= 60:
        print("Your grade is D.")
    else:
        print("Your grade is F.")
except ValueError:
    print("Please enter a valid number.")

# Prompting the user for input
score = float(input("Enter a score between 0.0 and 1.0: "))

# Checking if the score is within the valid range
if score < 0.0 or score > 1.0:
    print("Error: Score must be between 0.0 and 1.0")
else:
    # Determining the grade based on the score
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"

    # Printing the grade
    print(grade)

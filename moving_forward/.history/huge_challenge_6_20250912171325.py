#🔥 Challenge 3: Grade Converter

# Ask the user to enter a grade (0–100).

# Store the grade in a list.

# Use match with guards to classify it:

# 90–100 → "A"

# 80–89 → "B"

# 70–79 → "C"

# 60–69 → "D"

# Below 60 → "F"

# Use a boolean variable to check if the grade is passing (>= 60).

# Print the grade letter and pass/fail.

user_grade = int(input("Enter a number (grade) between 0-100: "))
user_grade_list = []
user_grade_list.append(user_grade)

match user_grade:  
    case usrg if 90 <= usrg <= 100:
        classification = "Pass"
        print("A")
    case usrg if 80 <= usrg <= 89:
        classification = "Pass"
        print("B")
    case usrg if 70 <= usrg <= 79:
        classification = "Pass"
        print("C")
    case usrg if 60 <= usrg <= 69:
        classification = "Pass"
        print("D")
    case usrg if usrg < 60:
        classification = "Fail"
        print("F")
    
grade_checker = user_grade >= 60

print("-------FINAL REPORT-------")
print("You", classification)



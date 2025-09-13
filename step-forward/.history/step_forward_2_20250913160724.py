# Challenge 2: Grade Checker

# Take an input number between 0–100.

# Use match with guards (case) to print:

# 90–100 → "A"

# 80–89 → "B"

# 70–79 → "C"

# 60–69 → "D"

# Below 60 → "F"

user_grade = int(input("Enter a number between 0 - 100: "))

grade = None

match user_grade:
    case usrg if 90 <= usrg <= 100:
        grade = "A"
    case usrg if 80 <= usrg <= 89:
        grade = "B"
    case usrg if 70 <= usrg <= 79:
        grade = "C"
    case usrg if 60 <= usrg <= 69:
        grade = "D"
    case usrg if usrg < 60:
        grade = "F"
    case _:
        print("Invalid number, try again")

print("Your grade is: ", grade)
        
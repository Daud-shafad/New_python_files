# Ask the user to enter a letter grade (A, B, C, D, F).
# Use a match statement to print: "Excellent" for A, "Good" for B, "Average" for C
# "Poor" for D, "Fail" for F, "Invalid grade" for any other input

grade = str(input("Please Enter your grade: "))
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")








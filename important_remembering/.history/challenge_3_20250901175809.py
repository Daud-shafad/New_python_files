# Ask the user to enter a grade letter (A, B, C, D, F). Use a match statement to print:

# "Excellent" for A

# "Good" for B

# "Average" for C

# "Poor" for D

# "Fail" for F

# "Invalid grade" for anything else.

grade = input("Enter your grade: ").upper()
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
        print("Invalid Grade")
         
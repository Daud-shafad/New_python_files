# Write a program that takes a grade (A, B, C, D, F) and prints a message. Example: "A" → "Excellent", "F" → "Fail".
grades = str(input("Enter your grade: "))
if grades == "A":
    print("Excellent!")
elif grades == "B":
    print("Good!")
elif grades == "C":
    print("Average!")
elif grades == "D":
    print("Below Average!")
elif grades == "F":
    print("Fail!")
else:
    print("no more talk!")
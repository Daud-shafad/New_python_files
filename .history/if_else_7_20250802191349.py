# Write a program that takes a grade (A, B, C, D, F) and prints a message. Example: "A" → "Excellent", "F" → "Fail".
grades = ["A", "B", "C", "D", "F"]
if "A" in grades:
    print("Excellent!")
elif "B" in grades:
    print("Good!")
elif"C" in grades:
    print("Average!")
elif "D" in grades:
    print("Below Average!")
elif "F" in grades:
    print("Fail!")
else:
    print("no more talk!")
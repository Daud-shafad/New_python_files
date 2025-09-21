# Challenge 2: Student Grade Analyzer

# Keep asking user (while loop) for student names and scores (0–100).

# Store scores in a dictionary with names as keys.

# Keep all scores in a list for analysis.

# Convert input to integer (casting).

# Use if/else or match with guards to categorize grades:

# 90–100 → "A"

# 80–89 → "B"

# 70–79 → "C"

# 60–69 → "D"

# <60 → "F"

# Calculate average score (operators, numbers) 
# and print a summary tuple of counts per grade.

# Challenge 12: Student Grade Analyzer
students = {}
scores = []

while True:
    name = input("Enter student name (or 'stop'): ")
    if name == "stop":
        break
    score = int(input("Enter score: "))
    students[name] = score
    scores.append(score)

for n, s in students.items():
    match s:
        case x if x >= 90:
            grade = "A"
        case x if x >= 80:
            grade = "B"
        case x if x >= 70:
            grade = "C"
        case x if x >= 60:
            grade = "D"
        case _:
            grade = "F"
    print(n, "->", grade)

average = sum(scores) / len(scores)
print("Average Score:", average)
print("Grades Summary Tuple:", tuple(students.values()))

 
    
            


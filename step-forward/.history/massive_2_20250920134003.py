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

while True:
    student_name = input("Enter your name: ")
    student_score = int(input("Enter your score as 0-100: "))
    student_dict = {}
    student_dict.update({student_name: student_score})
    student_scores_list = []
    student_scores_list.append(student_score)
    
    match student_score:
        case stds if 90 < stds < 100:
            grade = "A"
        case stds if 80 < stds < 89:
            grade = "B"
        case stds if 70 < stds < 79:
            grade = "C"
        case stds if 60 < stds < 69:
            grade = "D"
        case stds if  stds < 60:
            grade = "F"
 
    
            


# 🔥 Challenge: Grade Analyzer Mini-System

# Ask the user to enter 3 student grades (numbers, e.g. "85", "72", "90").

# Cast them from strings to integers.

# Store the grades in a list.

# Convert the list to a tuple to make it immutable.

# Make a set of the grades to keep unique values.

# Create a dictionary where the keys are "Grade1", "Grade2", "Grade3" 
# and the values are the grades.

# Use operators to calculate the average grade.

# Use if/else to check if the average is >= 50 (Pass) or < 50 (Fail).

# Use a boolean variable (e.g. is_high) to check if the highest grade is above 90.

# Use a match statement to classify the average:

# 90–100 → "Excellent"

# 70–89 → "Good"

# 50–69 → "Average"

# below 50 → "Poor"

# Finally, print all the collected data: list, tuple, set, dictionary, average, boolean, 
# and classification.

student_1_grade = int(input("Enter Your grade as student 1: "))
student_2_grade = int(input("Enter your grade as student 2: "))
student_3_grade = int(input("Enter your grade as student 3: "))

all_students_grades = []
all_students_grades.append(student_1_grade)
all_students_grades.append(student_2_grade)
all_students_grades.append(student_3_grade)
tuple_all_students_grades = tuple(all_students_grades)

set_all_students_grades_unique = set(all_students_grades)
dict_all_students_grades = ({"Grade-1" : student_1_grade, "Grade-2" : student_2_grade, "Grade-3" : student_3_grade}) 



average_grade = (student_1_grade + student_2_grade + student_3_grade) / 3


if  average_grade >= 50:
    print("Pass")
elif average_grade < 50:
    print("Fail")
    
    
is_high = student_1_grade > 90 or student_2_grade > 90 or student_3_grade > 90

match average_grade:
    case avg if 90 <= avg <= 100:
        print("Excellent")
    case avg if 70 <= avg <= 89:
        print("Good")
    case avg if 50 <= avg <= 69:
        print("Average")
    case avg if avg < 50:
        print("Poor")

         
print("\n-------FINAL REPORT-------")
print(all_students_grades)
print(tuple_all_students_grades)
print(set_all_students_grades_unique)
print(dict_all_students_grades)
print(average_grade)
print(is_high)  


#another way of dictionaries
#dict_all_students_grades.update({"Grade-1" : student_1_grade, "Grade-2" : student_2_grade, "Grade-3" : student_3_grade})
          
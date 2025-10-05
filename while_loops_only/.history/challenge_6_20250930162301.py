#  Main Challenge

# Create a dictionary called students that stores 
# 3 student names as keys 
# and their marks as numbers.
#  Use a while loop to keep checking each student’s marks:

# If marks are >= 50, set the value for that student’s key to True (pass).

# If marks are < 50, set the value to False (fail).
# Stop the loop after all students are checked.
# Finally, print the updated dictionary showing student name → pass/fail (True/False).

# Initial dictionary with students and their marks
students = {
    "Ali": 78,
    "Hassan": 45,
    "Maryam": 60
}

names = list(students.keys())
i = 0

while i < len(names):
    name = students[i]
    marks = students[name]
    
    if marks >= 50:
        students[name] = True
    else:
        students[name] = False
        
        i+=1
        
print(students)




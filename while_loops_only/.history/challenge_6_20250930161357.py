#  Main Challenge

# Create a dictionary called students that stores 
# 3 student names as keys 
# and their marks as numbers.
#  Use a while loop to keep checking each student’s marks:

# If marks are >= 50, set the value for that student’s key to True (pass).

# If marks are < 50, set the value to False (fail).
# Stop the loop after all students are checked.
# Finally, print the updated dictionary showing student name → pass/fail (True/False).

students = {
    "ahmed" : 78,
    "fatima" : 64,
    "abdirahman" : 48
}

while True:
    if students["ahmed"] >= 50:
        students.update({"passed"})
    elif students["ahmed"] < 50:
        students.update({})
    elif students["fatima"] >= 50:
        students.update({})
    elif students["fatima"] < 50:
        students.update({})
    elif students["abdirahman"] >= 50:
        students.update({})
    elif students["abdirahman"] < 50:
        students.update({})
    else:
        print("error, try again")
        
    print(students)
    
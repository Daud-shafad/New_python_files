# Scenario:
# You are building a simple School Student Management System that stores information about students, their grades, and subjects.
# The program should allow adding students, checking their results, and printing a summary report.

# Requirements:
# Variables – Create variables for school name, maximum students allowed, and a welcome message.

# Data Types – Use integers, floats, strings, booleans, and lists to store and process data.

# Numbers & Operators – Calculate average grades for students using arithmetic operators.

# Casting – Convert user inputs to integers/floats when entering marks.

# Strings – Format and display messages using string concatenation, f-strings, or .format().

# Booleans – Store pass/fail status for each student.

# Lists – Store student names and their grades in lists.

# Tuples – Store immutable subject names in a tuple (e.g., ("Math", "Science", "English")).

# Sets – Store unique student IDs in a set to prevent duplicates.

# Dictionaries – Store student details in a dictionary with keys like name, grades, and status.

# If-Else Statements – Check if a student has passed (average grade >= 50) or failed.

# Match Statement – Create a simple menu with options like:

# "1" → Add a student

# "2" → View all students

# "3" → Exit program

# While Loop – Keep asking the user for menu options until they choose to exit.

# Extra Rule – No functions allowed (just one main program flow).

# Final Output – When exiting, print a report showing:

# Total students added

# Each student’s name, ID, grades, and pass/fail status.


# School Student Management Program

# Step 1: Variables & Data Types
school_name = "Green Valley High School"
total_students = 0  # integer
average_score = 0.0  # float
is_open = True  # boolean

# Step 2: Lists, Tuples, Sets, Dictionaries
students = []  # list for storing student names
subjects = ("Math", "Science", "English")  # tuple of subjects
registered_ids = set()  # set to avoid duplicate IDs
student_data = {}  # dictionary to store student details

# Step 3: While loop for menu
while True:
    print("\n--- School Management Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Step 4: Match Statement for menu selection
    match choice:
        case "1":
            # Add Student
            student_id = input("Enter Student ID: ")
            if student_id in registered_ids:
                print("❌ Student ID already exists!")
            else:
                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))  # casting to integer
                score = float(input("Enter Average Score: "))  # casting to float

                # Boolean check with if-else
                if score >= 50:
                    passed = True
                else:
                    passed = False

                # Update data
                registered_ids.add(student_id)
                students.append(name)
                student_data[student_id] = {
                    "name": name,
                    "age": age,
                    "score": score,
                    "passed": passed
                }
                total_students += 1

                print(f"✅ Student {name} added successfully!")
        
        case "2":
            # View Students
            if total_students == 0:
                print("No students registered yet.")
            else:
                print(f"\nList of Students in {school_name}:")
                for sid, details in student_data.items():
                    print(f"ID: {sid} | Name: {details['name']} | Age: {details['age']} | Score: {details['score']} | Passed: {details['passed']}")
        
        case "3":
            # Search Student
            search_id = input("Enter Student ID to search: ")
            if search_id in student_data:
                details = student_data[search_id]
                print(f"✅ Student Found: {details}")
            else:
                print("❌ Student not found.")
        
        case "4":
            print("Exiting program... Goodbye!")
            break
        
        case _:
            print("Invalid choice, please try again.")






    
    

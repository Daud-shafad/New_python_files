# Day 3: Dictionaries + lists → student grade tracker

# Challenge 5: Student Grade Tracker (Dictionaries + Lists)

# Create an empty dictionary to store student data.

# Use a while loop to show menu: "1. Add Student", "2. Add Grade", 

# "3. View Grades", "4. Exit".

# Use if/else to handle exit condition.

# Use match statement for other choices:

# Choice 1: Ask for student name and create empty list for their grades

# Choice 2: Ask for student name and grade, add grade to student's list

# Choice 3: Ask for student name, show all their grades and average

# Handle cases where student doesn't exist.

# optional bonus steps:

# Add an option 5: View All Students.

# Add a simple password system before entering menu (for challenge).

stud_data_dict = {}

entry_password = "admin123"

while True:
    
    
    user_password = input("Enter the password: ").lower()
    if user_password != entry_password:
       print("Wrong password, start it again")
       break
   
    else:
     print("\n1. Add Student")
     print("2. Add Grade")
     print("3. View Grades")
     print("4. View All Students")
     print("5. Exit")
    
    user_choice = input("Enter a number between 1-5: ")
    
    if user_choice == '5':
        print("Goodbye!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        match user_choice:
            case '1':
                user_name = input("Enter student name: ")
                if user_name not in stud_data_dict:
                    stud_data_dict[user_name] = []  # Create empty list for grades
                    print(f"Student '{user_name}' added successfully!")
                else:
                    print(f"Student '{user_name}' already exists!")
                    
            case '2':
                user_name = input("Enter student name: ")
                if user_name in stud_data_dict:
                    user_grade = float(input("Enter grade: "))
                    stud_data_dict[user_name].append(user_grade)
                    print(f"Grade {user_grade} added for {user_name}!")
                else:
                    print(f"Student '{user_name}' not found! Add student first.")
                    
            case '3':
                user_name = input("Enter student name: ")
                if user_name in stud_data_dict:
                    grades = stud_data_dict[user_name]
                    if grades:
                        average = sum(grades) / len(grades)
                        print(f"Grades for {user_name}: {grades}")
                        print(f"Average: {average:.2f}")
                    else:
                        print(f"No grades found for {user_name}")
                else:
                    print(f"Student '{user_name}' not found!")
                    
            case '4':
                print(f"All Students data: {stud_data_dict}")
    else:
        print("Invalid choice, please enter 1-5")
      
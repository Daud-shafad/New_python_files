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

stud_data_dict = {}

while True:
    print("\n 1. Add Student")
    print("\n 2. Add Grade")
    print("\n 3. View Grades")
    print("\n 4. Exit")
    
    user_choice = input("Enter a number between 1-4: ")
    if user_choice == '4':
        print("You stopped the program")
        break
    elif user_choice == '1' or '2' or '3':
        match user_choice:
            case '1':
                user_name = input("Enter your name: ")
                empty_list = []
                empty_list.append(user_name)
                print("You added:", empty_list)
            case '2':
                user_name = input("Enter your name: ")
                user_grade = input("Enter your grade: ").upper()
                empty_list.append(user_grade)
                print("You added:", empty_list)
            case '3':
                user_name = input("Enter your name: ")
                stud_data_dict.update({user_name: user_grade})
                print(stud_data_dict)
                
            case _:
                print("Invalid input, enter 1-4")
    else:
        print("Invalid choice, try again")
                
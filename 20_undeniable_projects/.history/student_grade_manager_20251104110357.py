# Challenge 1: Student Grade Manager
# Combine: lists, dictionaries, if/else, while, match, strings, numbers

# Store students in dictionary: {name: [grades]}

# Menu: Add student, Add grade, View average, Exit

# Use while loop + match + if/else for all operations

student_grade_manager = {}

while True:
    print("\n-------Available Student Management Menu Options:-------")
    print("1. Add student")
    print("2. Add grade")
    print("3. View Average")
    print("4. Exit")
    
    student_choice = input("Enter Your choice: ")
    if student_choice == '4':
        print("See You later! You Exit the system")
        break
    elif student_choice == '1' or student_choice == '2' or student_choice == '3':
        
        match student_choice:
        
           case '1':
               student_name = 
               
        
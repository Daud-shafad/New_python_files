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
               student_name = input("Enter Your name: ")
               if student_name not in student_grade_manager:
                  student_grade_manager[student_name] = []
                  print(f"You added {student_name} Successfully")
               else:
                  print(f"Student name {student_name} is already exist")
            
           case '2':
                student_name = input("Enter Your name: ")
                student_grade = input("Enter Your grade: ")
                if student_name in student_grade_manager:
                    student_grade_manager[student_name] = [student_grade]
                    print(f"You added {student_grade} as grade for {student_name}")
                else:
                    print(f"Student name {student_name} was not found, Add it firstly")
            
           case '3':
                student_name = input("Enter Your name: ")
                if student_name in student_grade_manager:
                    average = sum(student_grade) / len(student_grade)
                    print(f"Your average is: {average}")
                else:
                    print(f"Student name {student_name} was not found")
            
           case _:
                print("Invalid option, Try again")
    
    else:
        print("Invalid choice menu, Type (1-4)")
               
        
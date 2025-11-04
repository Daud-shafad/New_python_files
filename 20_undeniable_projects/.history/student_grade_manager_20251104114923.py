# Challenge 1: Student Grade Manager
# Combine: lists, dictionaries, if/else, while, match, strings, numbers

# Store students in dictionary: {name: [grades]}

# Menu: Add student, Add grade, View average, View student, Exit

# Use while loop + match + if/else for all operations

student_grade_manager = {}

while True:
    print("\n-------Available Student Management Menu Options:-------")
    print("1. Add student")
    print("2. Add grades")
    print("3. View Student")
    print("4. View Average")
    print("5. Exit")
    
    student_choice = input("Enter Your choice: ")
    if student_choice == '5':
        print("See You later! You Exit the system")
        break
    elif student_choice == '1' or student_choice == '2' or student_choice == '3' or student_choice == '4':
        
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
                student_grades = input("Enter Your grades: ")
                if student_name in student_grade_manager:
                    student_grade_manager[student_name] = [student_grades]
                    print(f"You added {student_grades} as grades for {student_name}")
                else:
                    print(f"Student name {student_name} was not found, Add it firstly")
            
           case '3':
                student_name = input("Enter Your name: ")
                if student_name in student_grade_manager:
                   print(student_grade_manager[student_name])
                else:
                   print("Student name {student_name} was not found")
           
           case '4':
                student_name = input("Enter Your name: ")
                if student_name in student_grade_manager:
                    total = student_grade_manager[student_name] 
                  
                    average = sum(total) / len(total)
                    print(f"Your average is: {average}")
                else:
                    print(f"Student name {student_name} was not found")
            
           case _:
                print("Invalid option, Try again")
    
    else:
        print("Invalid choice menu, Type (1-4)")
               
        
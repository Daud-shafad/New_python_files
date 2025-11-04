# Challenge 1: Student Grade Manager
# Combine: lists, dictionaries, if/else, while, match, strings, numbers

# Store students in dictionary: {name: [grades]}

# Menu: Add student, Add grade, View average, View student, Exit

# Use while loop + match + if/else for all operations

student_grade_manager = {}

while True:
    print("\n-------Available Student Management Menu Options:-------")
    print("1. Add student")
    print("2. Add grade")
    print("3. View Student")
    print("4. View All Students")
    print("5. View Min/Max/Average grades")
    print("6. Exit")
    
    student_choice = input("Enter Your choice: ")
    if student_choice == '6':
        print("See You later! You Exit the system")
        break
    elif student_choice == '1' or student_choice == '2' or student_choice == '3' or student_choice == '4' or student_choice == '5':
        
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
                student_grade = float(input("Enter Your grade: "))
                if student_name in student_grade_manager:
                    student_grade_manager[student_name].append(student_grade)
                    print(f"You added {student_grade} as grades for {student_name}")
                else:
                    print(f"Student name {student_name} was not found, Add it firstly")
            
           case '3':
                student_name = input("Enter Your name: ")
                if student_name in student_grade_manager:
                  # student_grade_manager[student_name]
                   print(f"All your grades are: {student_grade_manager[student_name]}")
                else:
                   print("Student name {student_name} was not found")
           
           case '4':
                   print(student_grade_manager)
                   
           case '5':
                student_name = input("Enter Your name: ")
                if student_name in student_grade_manager:
                   all_grades = student_grade_manager[student_name]
                   print("-------You have the following DATA of:--------")
                   print("Your max grade is:", max(all_grades))
                   print("Your max grade is:",  min(all_grades))
                   print("Your average is:",  sum(all_grades) / len(all_grades))
                   
                   
                else:
                    print(f"Student name {student_name} was not found")
            
           case _:
                print("Invalid option, Try again")
    
    else:
        print("Invalid choice menu, Type (1-4)")
               
        
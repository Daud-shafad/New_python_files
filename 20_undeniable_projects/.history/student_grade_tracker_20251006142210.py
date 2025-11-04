# student grade tracker using lists, dictionaries, if/else, match, & while loop

students_records_dict = {}

while True:
    print("\n-----Available Menu Options-----:")
    print("\n 1. Add Student")
    print("2. Add Grade")
    print("3. View Student")
    print("4. View All student")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
        print("Good bye, you stop it!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        match user_choice:
            case '1':
                student_name = input("Enter Your name: ")
                if student_name not in students_records_dict:
                    students_records_dict[student_name] = []
                    print(f"New student {student_name} was Added successfully")
                else:
                    print("Student name is Already exists")
                    
            case '2':
                student_name = input("Enter your name: ")
                student_grade = float(input("Enter Your grade: "))
                students_records_dict[student_name].append(student_grade)
                print(f"New grade {student_grade} was Added Successfully")
                
            case '3':
                student_name = input("Enter Your name: ")
                if student_name in students_records_dict:
                    students_records_dict[student_name]
                    print(f"The grades of this student is {students_records_dict[student_name]}")
                    print(sum(students_records_dict[student_name]))
                    
                    
                else:
                    print("Student not Found, Add the Student Firstly")
                    
            case '4':
                print(f"The Students records we have is {students_records_dict}")
                
            case _:
                print("Invalid Choice, type (1-5)")
    else:
        print("Invalid Choice, Try again")    
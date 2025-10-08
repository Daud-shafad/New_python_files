# in here i am making simple employee_management_system
# this system contains, adding, viewing, updating salaries
# also this system is only contains, while loop, variables, if/else, match statements
# also it contains python core concepts like:
# dictionaries, lists, variables, casting, inputs, outputs
# at the end of this program you can add, update salary, view-specific, view all
# employees, so let's start it.

employee_dict = {}



while True:
    print("-----Available option menus:----- ")
    print("\n 1. Add Employee")
    print("2. Update Salary")
    print("3. View S.Employee")
    print("4. View All Employees")
    print("5. Exit")
    
    user_choice = input("Enter Your Choice (1-5): ")
    if user_choice == '5':
        print("Good bye, You stopped the program")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
    
       match user_choice:
          case '1':
            emp_id = int(input("Enter Your ID: "))
            emp_name = input("Enter Your name: ")
            emp_dept = input("Enter Your department: ").upper()
            emp_salary = int(input("Enter Your salary: "))
            if emp_id not in employee_dict:
                employee_dict[emp_id] = [emp_name, emp_dept, emp_salary]
                print(f"New ID {emp_id} was Successfully Added.")
            else:
                print("The ID you Entered is Already existed")
                
          case '2':
            emp_id = int(input("Enter Your ID: "))
            emp_new_salary = int(input("Enter Your new salary: "))
            if emp_id in employee_dict:
                employee_dict[emp_salary] = (emp_new_salary)
                print(employee_dict[emp_new_salary])
                print(f"Salary was updated {emp_id}, with a value of {emp_new_salary}")
            else:
                print("Employee not found, Add it firstly")
                
          case '3':
            emp_id = int(input("Enter Your ID: "))
            if emp_id in employee_dict:
                print(f"The ID of {emp_id} has a data of: {employee_dict[emp_id]}")
            else:
                print("not found, Add it firstly")
                
          case '4':
                print(f"The data you're requesting is: {employee_dict}")
        
          case _:
                print("Invalid choice, Try again")
    else:
        print("Invalid choice, Type (1-5)")
                
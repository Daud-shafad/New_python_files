## Challenge: Employee Management System

# Create an employee management system using dictionaries and lists.
# The dictionary should store: employee_id as key, and [name, department, salary] as value.
# Menu Options:
# 1. Add Employee (ask for id, name, department, salary)
# 2. Update Salary (ask for employee id and new salary)
# 3. View Employee Details (ask for employee id)
# 4. View All Employees in Department (ask for department name)
# 5. Exit
# Use while loop for menu, if/else for conditions, and match for menu options.
# Example structure:
# employees = {
# 101: ["John", "IT", 50000],
# 102: ["Sarah", "HR", 45000] }

employee_man_dict = {}

while True:
    print("\n 1. Add Employee")
    print("2. Update Salary")
    print("3. View Employee")
    print("4. View All Employees")
    print("5. Exit")
    
    user_choice = input("Enter you choice (1-5): ")
    if user_choice == '5':
        print("You stop it the program, goodbye")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        match  user_choice:
            case '1':
                emp_id = int(input("Enter Your ID: "))
                emp_name = input("Enter your name:")
                if emp_id not in employee_man_dict:
                   employee_man_dict[emp_id] = []
                   employee_man_dict[emp_id].append(emp_name)
                   print(f"New Employee {emp_id} Added Successfully.")
                else:
                    print(f"Employee Already exists {emp_id} choose another option.")
            case '2':
                emp_id = int(input("Enter Your ID: "))
                if emp_id in employee_man_dict:
                    emp_name = input("Enter Your name: ")
                    emp_dept = input("Enter Your department: ").upper()
                    emp_salary = int(input("Enter the new salary: "))
                    employee_man_dict[emp_id].append(emp_salary)
                    print(f"Salary Was Updated {emp_id} With Value Of {emp_salary}")
                else:
                    print("Add Employee Firstly")
            case '3':
                emp_id = int(input("Enter Your ID: "))
                if emp_id in employee_man_dict:
                    employee_man_dict.items({emp_id :[emp_name, emp_dept, emp_salary]})
                    print(employee_man_dict)
                else:
                    print("Add the Employee firstly")
            case '4':
                    employee_man_dict.items({emp_id :[emp_name, emp_dept, emp_salary]})
                    print(employee_man_dict)
            case _:
                    print("Invalid option choose (1-5)")
    else:
        print("Invalid choice, try again")
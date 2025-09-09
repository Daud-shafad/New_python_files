# Challenge Idea:

# Build a student management mini-system that:

# Asks the user to input a student’s name and age (use variables).

# Stores the names inside a list, and ages inside a tuple.

# Creates a dictionary where each student’s name is the key and their age is the value.

# Keeps a set of all unique ages entered.

# Uses casting (e.g., convert input string → integer for age).

# Uses if/else to check conditions (e.g., if age ≥ 18 → “adult”, else → “minor”).

# Uses booleans + operators to test (e.g., if student age is >= 18 and <= 25).

# Shows the final stored data (output everything clearly).


student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_name_list = []
student_name_list.append(student_name)
student_age_tuple = ()
student_age_workaround_tuple = []
student_age_workaround_tuple.append(student_age)
student_age_tuple = tuple((student_age_workaround_tuple))
student_dict = {}
student_dict.update({student_name : student_age})
student_set_unique_ages = set(student_age_tuple)

if student_age >= 18:
    print("Adult")
else:
    print("Minor")
    
check_student_age = student_age >= 18 and student_age <= 25
print(check_student_age)

print("\n-------FINAL REPORT-------")
print(student_name_list)
print(student_age_tuple)
print(student_dict)
print(student_set_unique_ages)



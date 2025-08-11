# Challenge: Simple Student Registration System
# Steps

# Create variables to store a student's name, age, and GPA (Grade Point Average).

# Use casting to ensure age is an integer and GPA is a float.

# Store the student's favorite subjects in a list.

# Store the student’s permanent subjects in a tuple.

# Store the set of extracurricular activities (no duplicates allowed) in a set.

# Store student’s information in a dictionary (keys: name, age, GPA, subjects, activities).

# Use a while loop to keep the program running until the user types "exit".

# Inside the loop, ask the user what they want to do: "view", "update", "add", or "exit".

# Use a match statement to handle the choice.

# For "view", display all student information from the dictionary.

# For "update", ask the user which field to change (name, age, GPA) and update it.

# For "add", allow the user to add a new activity to the set of activities.

# Use if/else inside "update" to handle wrong field names.

# Use if/else to handle invalid menu choices in the loop.

# End the program when "exit" is chosen.


# Simple Student Registration System

# Step 1 & 2: Basic student details with casting
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
gpa = float(input("Enter student's GPA: "))

# Step 3: List of favorite subjects
subjects = input("Enter favorite subjects (comma separated): ").split(",")

# Step 4: Tuple for permanent subjects
permanent_subjects = ("Math", "English", "Science")

# Step 5: Set for extracurricular activities
activities = set(input("Enter extracurricular activities (comma separated): ").split(","))

# Step 6: Dictionary to store student info
student = {
    "name": name,
    "age": age,
    "gpa": gpa,
    "subjects": subjects,
    "permanent_subjects": permanent_subjects,
    "activities": activities
}

# Step 7: While loop for menu
while True:
    print("\nMenu: view / update / add / exit")
    choice = input("Enter your choice: ").lower()

    # Step 8 & 9: Match statement for menu options
    match choice:
        case "view":
            print("\n--- Student Information ---")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("GPA:", student["gpa"])
            print("Favorite Subjects:", student["subjects"])
            print("Permanent Subjects:", student["permanent_subjects"])
            print("Activities:", student["activities"])

        case "update":
            field = input("Which field do you want to update? (name/age/gpa): ").lower()
            # Step 13: If/else for updating
            if field == "name":
                student["name"] = input("Enter new name: ")
            elif field == "age":
                student["age"] = int(input("Enter new age: "))
            elif field == "gpa":
                student["gpa"] = float(input("Enter new GPA: "))
            else:
                print("Invalid field name.")

        case "add":
            new_activity = input("Enter new activity to add: ")
            student["activities"].add(new_activity)
            print("Activity added!")

        case "exit":
            print("Exiting program... Goodbye!")
            break

        case _:
            # Step 14: Invalid choice
            print("Invalid choice. Please try again.")



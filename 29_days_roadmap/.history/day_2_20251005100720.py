#  Day 2: If/Else + Match + While → menu-driven calculator.

# Challenge 4: Simple Menu-Driven Calculator

# Use a while loop to keep showing the calculator menu.

# The menu should have options: "1. Add", "2. Subtract", "3. Multiply", "4. Divide", "5. Exit".

# Use if/else to check if the user wants to exit (choice '5').

# Use a match statement to handle the calculation choices (1-4).

# For choices 1-4, ask for two numbers and perform the operation.

# For division, check if the second number is zero and show an error.

# If user enters invalid choice, show error message.

while True:
    print("\n 1. Addition (+)")
    print("\n 2. Subtraction (-)")
    print("\n 3. Multiplication (*)")
    print("\n 4. Division (/)")
    print("\n 5. Exit")
    
    user_choice = (input("Enter a number between 1-5: "))
    if user_choice == '5':
        print("You skip it!")
        break
    else:
        match user_choice:
          case '1':
            user_num_1 = float(input("Enter number 1: "))
            user_num_2 = float(input("Enter number 2: "))
            result = user_num_1 + user_num_2
            print("The result is: ", result)
          case '2':
            user_num_1 = float(input("Enter number 1: "))
            user_num_2 = float(input("Enter number 2: "))
            result = user_num_1 - user_num_2
            print("The result is: ", result)
          case '3':
            user_num_1 = float(input("Enter number 1: "))
            user_num_2 = float(input("Enter number 2: "))
            result = user_num_1 * user_num_2
            print("The result is: ", result)
          case '4':
            user_num_1 = float(input("Enter number 1: "))
            user_num_2 = float(input("Enter number 2: "))
            if user_num_2 != 0:
              result = user_num_1 / user_num_2
              print("The result is: ", result)
            else:
                print("Invalid, can't divide zero ")
          case _:
            print("Invalid choice, try again")
         
   
   
  
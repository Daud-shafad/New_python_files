# Ask the user to enter a number from 1 to 7.
# Use a match statement to print the name of the corresponding day of the week
# (1 = Monday, 2 = Tuesday, ..., 7 = Sunday).
# Print "Invalid day" if the number is not between 1 and 7.

number = int(input("Enter a number from 1 to 7: "))
match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
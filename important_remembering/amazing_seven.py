# Challenge 7: Day of the Week
# Ask for a number (1–7). Use match to print the day (1 = Monday, etc.).

number = int(input("Enter a number: "))
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
        print("Invalid number")
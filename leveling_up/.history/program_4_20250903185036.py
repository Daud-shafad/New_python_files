# Challenge 22: Day Checker (match + tuple + boolean)

# Store days of the week in a tuple.

# Ask user for a number 1–7.

# Use match to print the day.

# Add a boolean check: if day is Saturday or Sunday → print “Weekend”, else “Weekday”.

week_days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

user_number = int(input("Enter a number between 1-7: "))
match user_number:
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
        
day_checker = week_days("saturday", "sunday") = True
if day_checker: 
    print("Weekend")
else:
    print("Weekday")


# Challenge 18: Match with Days of the Week
# Ask the user to enter a number (1–7). 
# Use match to print the day of the week (1=Monday, 7=Sunday). If invalid, print "Not a valid day"

user_choice = int(input("Enter a number: "))
match user_choice:
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
     print("Not valid day")
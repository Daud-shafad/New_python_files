# Challenge 22: Day Checker (match + tuple + boolean)

# Store days of the week in a tuple.

# Ask user for a number 1–7.

# Use match to print the day.

# Add a boolean check: if day is Saturday or Sunday → print “Weekend”, else “Weekday”.

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

num = int(input("Enter a number (1–7): "))

if num >= 1 and num <= 7:
    day = days[num - 1]

    match num:
        case 6:
            print(day, "→ Weekend")
        case 7:
            print(day, "→ Weekend")
        case _:
            print(day, "→ Weekday")
else:
    print("Invalid input! Please enter 1–7.")



"""
Write a match statement that checks a variable day and prints:
"Weekday" if day is 1 to 5

"Weekend" if day is 6 or 7

"Invalid" for anything else
"""
day = int(input("the day of weeks in number: "))
match day:
    case 1:
        print("Weekday")
    case 2:
        print("Weekday")
    case 3:
        print("Weekday")
    case 4:
        print("Weekday")
    case 5:
        print("Weekday")   
    case 6:
        print("Weekend")
    case 7:
        print("Weekend")
    case_:
        print("Invalid")
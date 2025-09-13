# Challenge 1: Day Type Checker

# Ask the user to input a number (1–7).

# Store the days of the week in a tuple.

# Use match to print the corresponding day.

# Use a boolean + operator to check if it’s a weekend (Saturday or Sunday).

# Print the result.

user_number = int(input("Enter a number between 1-7: "))
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

match user_number:
    case 1:
        print(days_of_the_week[0])
    case 2:
        print(days_of_the_week[1])
    case 3: 
        print(days_of_the_week[2])
    case 4:
        print(days_of_the_week[3])
    case 5:
        print(days_of_the_week[4])
    case 6:
        print(days_of_the_week[5])
    case 7:
        print(days_of_the_week[6])
    case _:
        print("Invalid number, try again")
    
week_end_checker_1 =  user_number == days_of_the_week[5] or user_number == days_of_the_week[6]

print(week_end_checker_1)
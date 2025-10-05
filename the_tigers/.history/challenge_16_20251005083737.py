# Challenge 1: The Number Analyzer Loop

# Use a while loop to keep the program running.

# Ask the user to enter a number.

# Use if/else to check if the number is positive, negative, or zero and print the result.

# Use a match statement to print the day of the week 
# if the user enters a number from 1 (Monday) to 7 (Sunday). 
# If the number is outside this range, print "Invalid day".

# The loop should only break if the user types "quit".

while True:
    user_input = int(input("Enter a number: "))
    if user_input == "quit":
        break
    
    if user_input > 0: 
        print("positive") 
    elif user_input < 0:
        print("negative")
    elif user_input == 0:
        print("zero")
    
    match user_input:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case _:
            print("Invalid day")
else:
print()
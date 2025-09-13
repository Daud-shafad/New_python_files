# Challenge: Number Sign & Range Checker

# Ask the user to enter a number (input).

# Use operators to check if the number is positive, negative, or zero.

# Store the result in a boolean variable.

# Use a match statement to classify the number into:

# Negative

# Zero

# Positive (further check if greater than 100 or not).

# Print the result.

user_number = int(input("Enter a number: "))

check_number =  0 > user_number > 0 or user_number == 0

match check_number:
    case chk if 0 > chk:
        print("Negative")
    case chk if 0 == chk:
        print("Zero")
    case chk if 0 < chk > 100:
        print("Positive, it is greater than 100")
   

print(check_number)
        
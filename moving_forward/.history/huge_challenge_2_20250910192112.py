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

match user_number:
    case usr_n if 0 > usr_n:
        print("Negative")
    case usr_n if 0 == usr_n:
        print("Zero")
    case usr_n if 0 < usr_n > 100:
        print("Positive, it is greater than 100")
   

print(check_number)
        
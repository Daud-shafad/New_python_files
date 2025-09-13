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

check_number_1 =  0 > user_number 
check_number_2 =  0 == user_number
check_number_3 =  0 < user_number 

match user_number:
    case usr if 0 > usr:
        print("Negative")
    case usr if 0 == usr:
        print("Zero")
    case usr if usr > 100:
        print("Positive, also it is greater than 100")
    case usr if 0 < usr:
        print("Positive")
   

print("Negative", check_number_1)
print("Zero number", check_number_2)
print("Positive number", check_number_3)
        
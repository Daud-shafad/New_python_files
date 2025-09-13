# 🔥 Challenge 2: Even or Odd Classifier

# Ask the user to input a number.

# Store the number inside a list.

# Use match with guards (case n if ...) to check if it’s even or odd.

# Use a boolean to store the result.

# Print the classification and the boolean.

user_number = int(input("Enter a number: "))
user_number_list = []
user_number_list.append(user_number)

match user_number:
    case usrn if usrn % 2 == 0:
        classification = usrn == 0
    case usrn if usrn % 2 != 0:
        classification = usrn != 0
        
print(user_number)
print(user_number_list)
print("you entered an", classification, "number")
        
        
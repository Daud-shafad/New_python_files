#🔥 Challenge 5: Number Comparison

# Ask the user for two numbers.

# Store them in a tuple.

# Use match with guards to check:

# First > Second → "First is bigger"

# First < Second → "Second is bigger"

# Equal → "Both are equal"

# Use a boolean + operator to store whether the numbers are equal.

# Print the result and the boolean.


user_first_num_1 = int(input("Enter a number 1: "))
user_second_num_2 = int(input("Enter a number 2: "))

user_num_list = []
user_num_list.append(user_first_num_1)
user_num_list.append(user_second_num_2)
user_num_tuple = tuple((user_num_list))

match user_first_num_1, user_second_num_2:
    case usrn1_2 if user_first_num_1 > user_second_num_2:
        classification = "First is bigger"
    case usrn1_2 if user_second_num_2 > user_first_num_1:
        classification = "Second is bigger"
    case usrn1_2 if user_first_num_1 == user_second_num_2:
        classification = "Both are equal"
    
check_equality = user_first_num_1 == user_second_num_2

print("\n-------FINAL REPORT-------")
print(user_num_tuple)
print("the output of the comparison is: " , classification)
print("are both numbers equal? ", check_equality)
        
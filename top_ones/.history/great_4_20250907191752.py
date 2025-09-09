# Challenge 35: Ultimate Data Collector 
# (variables + lists + tuples + dictionaries + sets + if/else) 
# (casting + booleans + operators + inputs + outputs)

# Ask the user to enter 3 numbers using input.

# Cast the inputs from string to integers and store them in a list.

# Convert the list into a set to remove duplicates.

# Store the original 3 numbers as a tuple.

# Create a dictionary where the keys are the numbers and the values are "Even" or "Odd" based on the number.

# Use if/else and operators to check if the sum of the numbers is greater than 50.

# Store the result in a boolean variable is_large_sum.

# Print all of the following:

# The list of numbers entered

# The tuple of numbers

# The set of unique numbers

# The dictionary of numbers with "Even"/"Odd"

# The boolean result is_large_sum

user_inputs = int(input("Enter 3 numbers: ").split(","))

user_inputs_list = []
user_inputs_list.append(user_inputs)

user_inputs_set = set(user_inputs_list)
user_inputs_tuple = tuple(user_inputs)
dict_user_inputs = dict(user_inputs_list)
dict_user_inputs.setdefault({"even", "odd"})

                        


is_large_sum = user_inputs + user_inputs + user_inputs > 50
if is_large_sum:
    print(is_large_sum)
else:
    print(False)
    
print("\n---Final Report---")
print(user_inputs_list)
print(user_inputs_tuple)
print(user_inputs_set)
print(dict_user_inputs)




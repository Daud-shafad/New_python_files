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

user_input_1 = int(input("Enter number 1: "))
user_input_2 = int(input("Enter number 2: "))
user_input_3 = int(input("Enter number 1: "))

user_inputs_list = []
user_inputs_list.append(user_input_1)
user_inputs_list.append(user_input_2)
user_inputs_list.append(user_input_3)


user_inputs_set = set((user_inputs_list))
user_inputs_tuple_1 = tuple((user_input_1,))
user_inputs_tuple_2 = tuple((user_input_2,))
user_inputs_tuple_3 = tuple((user_input_3,))
all_user_original_inputs_tuple = (user_inputs_tuple_1 + user_inputs_tuple_2 + user_inputs_tuple_3)
dict_user_inputs = dict("even": "odd")


                        


is_large_sum = user_input_1 + user_input_2 + user_input_3 > 50
if is_large_sum:
    print(is_large_sum)
else:
    print(False)
    
print("\n---Final Report---")
print(user_inputs_list)
print(all_user_original_inputs_tuple)
print(user_inputs_set)
print(dict_user_inputs)




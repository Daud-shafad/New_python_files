# Challenge 1: Positive Numbers Collector

# Start with an empty list.

# Use a while loop to take numbers as input.

# If the number is positive, add it to the list.

# If negative, stop the loop and print the final list.

empty_list = []

while True:
    user_num = int(input("Enter a number: "))
    
    if user_num > 0:
        empty_list.append(user_num)
    else:
        break
print(empty_list)
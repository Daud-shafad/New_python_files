# Challenge 1: Positive Numbers Collector

# Start with an empty list.

# Use a while loop to take numbers as input.

# If the number is positive, add it to the list.

# If the number is equal to 0, tell the user try again

# If negative, stop the loop and print the final list.

empty_list = []

while True:
    user_num = int(input("Enter a number: "))
    
    if user_num > 0:
        empty_list.append(user_num)
    elif user_num == 0:
        print("Try again, Enter a normal number. ")
    else:
        break
    
print(empty_list)
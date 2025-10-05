# Start with an empty list for numbers.
# Use a while loop to take integer input from user.
# If number is positive and even, add to list and print "Added even"
# If number is positive and odd, add to list and print "Added odd"
# If number is zero, print "Zero ignored" and continue
# If number is negative, stop the loop
# Finally print the collected list and sum of all numbers in it

num_list = []

while True:
    user_num = int(input("Enter a number: "))
    if user_num > 0 and user_num % 2 == 0:
        num_list.append("Added even")
    elif user_num > 0 and user_num % 2 != 0:
        num_list.append("Added odd")
    elif user_num == 0:
        print("Zero ignored")
        
    else:
        break
print(num_list)
print(sum(num_list))
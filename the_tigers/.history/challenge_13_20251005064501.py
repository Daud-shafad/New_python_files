# Challenge 1: Find the Gap

#  Have a sorted list of numbers.
# Use while loop with index i < len(list)-1.
# Find the first gap where the difference between consecutive numbers is more than 1.
# When found, print "Gap found between [num1] and [num2]"
# If no gap found, print "No gaps in sequence".
# Example:

# [1, 2, 4, 5, 7] → "Gap found between 2 and 4"

num_list = [1,2,3,5,7,8,10,12,13,14]

i = 0

while i < len(num_list) - 1:
    if num_list[i] > num_list[i + 1] and num_list[i] < num_list[i-1]:
        print("gap found between", num_list[i], "and", num_list[i+1])
        break
    i+=1
else:
    print("no gap found")








# Challenge: Find Consecutive Duplicates
# Have a list of numbers.
# Use while loop with index i < len(list)-1.
# Find the first occurrence where two consecutive numbers are equal.
# When found, print "Consecutive duplicates found: [number] at positions [i] and [i+1]"
# If no consecutive duplicates found after checking all, 
# print "No consecutive duplicates".
# Example:
# [1, 3, 5, 5, 7, 9] → "Consecutive duplicates found: 5 at positions 2 and 3"
# [1, 2, 3, 4, 5] → "No consecutive duplicates"

num_list = [2,4,5,6,6,7,8,9]

i = 0

while i < len(num_list) - 1:
    if num_list[i] == num_list[i + 1]:
     print("Consecutive duplicates found:", num_list[i], "at positions", i, "and", i + 1)
     break
    i += 1
else:
    print("No consecutive duplicates")











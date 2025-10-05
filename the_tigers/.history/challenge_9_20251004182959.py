
# Challenge 2: Count Numbers Greater Than 10
# Have a list of numbers.
# Use while loop with index i < len(list).
# Count how many numbers are greater than 10.
# After loop finishes, print "Count: [count]"

num_list = [2,4,6,7,10,12,18,23,27]

i = 0
count = 0
while i < len(num_list):
     if num_list[i] > 10:
         count += 1
         i +=1
         print(count)
# Challenge 1: Find Divisible by 5

# Have a list of numbers 

# Use while loop with index i < len(list).

# Find the first number divisible by 5.

# When found, print "First divisible by 5: [number]" and stop.

# If none found, print "No number divisible by 5".

num_list = [3, 6, 5, 10, 12, 15, 18, 20]

i = 0

while i < len(num_list):
    if num_list[i] % 5 == 0:
        print("first divisible by 5: ", i)
        break
     i += 1
else:
    print("no divisible by 5 / not found")
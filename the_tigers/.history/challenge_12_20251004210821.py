# Challenge: Find the Peak Element

# Have a list of numbers representing heights.

# Use while loop with index i < len(list).

# Find the first number that is greater than both its neighbors.

# When found, print "Peak found: [number] at position [i]"

# If no peak found after checking all, print "No peak found".

# Note: Skip the first and last elements since they don't have both neighbors.

# Example:

#  `[1, 3, 2, 5, 4]` → "Peak found: 3 at position 1"

# - `[1, 2, 3, 4, 5]` → "No peak found"

num_list = [2,4,5,6,7,5,9,10,11,13]
i = 1  

while i < len(num_list) - 1:  
    if num_list[i] > num_list[i - 1] and num_list[i] > num_list[i + 1]:
        print("Peak found:", num_list[i], "at position", i)
        break
    i += 1
else:
    print("No peak found")

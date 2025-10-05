# Challenge 2: Find the Valley

# Have a list of numbers.
# Use while loop with index i < len(list).
# Find the first number that is smaller than both its neighbors.
# Print "Valley found: [number] at position [i]" or "No valley found".
# Note: Skip first and last elements.

num_list = [3,4,6,14,9,10,13]
i = 1
while i <= len(num_list):
    if num_list[i] < num_list[i+1] and num_list[i] < num_list[i-1]:
        print("valley found:" , i, "at position", num_list[i])
        break
    i += 1
else:
    print("No valley found")
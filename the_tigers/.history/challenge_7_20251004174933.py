# Have a list of numbers with both positive and negative values.
# Use a while loop with index i < len(list) to search through the list.
# Find the first negative number in the list.
# When found, print "First negative found: [number]" and stop searching.
# If no negative number is found after checking all, print "No negatives found".

num_list = [1, 3, 4, 9, 6, 5, 8, 7]

i = 0

while i < len(num_list):
    if num_list[i] < 0:
        print("first negative is found", i)
        break
    i += 1
else:
    print("no negatives found")
    
    
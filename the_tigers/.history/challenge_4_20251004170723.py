#  Challenge 4: Search for a Value

# Have a list of numbers.

# Use a while loop with index to search for a specific number stored in a variable.

# If found, print "Found" and stop the loop.

# If the loop finishes without finding it, print "Not Found".

numbers = [10, 20, 30, 40, 50]
target = 30
found = False
index = 0

while index < len(numbers):
    if numbers[index] == target:
        found = True
        break
    index += 1

if found:
    print("Found")
else:
    print("Not Found")
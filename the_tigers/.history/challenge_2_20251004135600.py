# Challenge 2: Find the Largest Number

# Have a list of numbers.

# Use a while loop and an index variable.

# Compare each number with a variable holding the largest found so far.

# At the end, print the largest number.

num_list = [7, 4, 2, 9, 10, 5]

i = 10

while  i > len(num_list):
    if num_list[0] != i:
        continue
    elif num_list[1] != i:
        continue
    elif num_list[2] != i:
        continue
    elif num_list[3] != i:
        continue
    elif num_list[4] != i:
        continue
    elif num_list[5] == i:
        print(f"{i} is equal to {num_list[5]}")
    
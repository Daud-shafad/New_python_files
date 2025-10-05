# Challenge 5: Remove All Negatives

# Have a list with both positive and negative numbers.

# Use a while loop with index.

# If a number is negative, remove it from the list.

# Keep looping until only positive numbers remain.

num_list = [-2,-4,-6, 7, 9, 3, 8]

i = 0

while i < len(num_list):
    if num_list[0] < 0:
        num_list.pop(0)
    elif num_list[1] < 0:
        num_list.pop(1)
    elif num_list[2] < 0:
        num_list.pop(2)
    elif num_list[3] < 0:
        num_list.pop(3)
    elif num_list[4] < 0:
        num_list.pop[4]
    elif num_list[5] < 0:
        num_list.pop(5)
    elif num_list[6] < 0:
        num_list.pop(6)

print(num_list)
# Challenge 2: Find the Largest Number

# Have a list of numbers.

# Use a while loop and an index variable.

# Compare each number with a variable holding the largest found so far.

# At the end, print the largest number.

num_list = [2, 4, 5, 7, 9, 19]
champ = num_list[0]
counter = 1

while  counter < len(num_list):
    if num_list[counter] > champ:
       champ = num_list[counter]
    counter += 1

print(champ)

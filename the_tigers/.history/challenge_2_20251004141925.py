# Challenge 2: Find the Largest Number

# Have a list of numbers.

# Use a while loop and an index variable.

# Compare each number with a variable holding the largest found so far.

# At the end, print the largest number.

num_list = [7, 4, 2, 9, 10, 5]
champ = 10

while  champ > len(num_list):
    if num_list[0] == champ:
        champ = num_list[0]
    elif num_list[1] == champ:
        print("found")
    elif num_list[2] == champ:
        print("found")
    elif num_list[3] == champ:
        print("found")
    elif num_list[4] == champ:
        print("found")
    elif num_list[5] == champ:
        print(f"{champ} is equal to {num_list[5]} which is 10")
    
print("largest number is", champ)
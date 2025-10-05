# Challenge 3: Count Even and Odd Numbers

# Have a list of numbers.

# Use a while loop with index.

# Use if/else to check whether each number is even or odd (% operator).

# Print the count of even and odd numbers separately.

num_list = [8,4,5,2,9]

even = 0
odd = 0
i = 1

while i < len(num_list):
    if num_list[i] % 2 == 0:
        even += 1
        print(even)
    else:                                    
        odd += 1
        print(odd)
        
        
        
        num_list = [2, 4, 5, 7, 9, 19]
champ = num_list[0]
counter = 1

while  counter < len(num_list):
    if num_list[counter] > champ:
       champ = num_list[counter]
    counter += 1

print(champ)

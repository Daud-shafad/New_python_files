# Challenge 3: Count Even and Odd Numbers

# Have a list of numbers.

# Use a while loop with index.

# Use if/else to check whether each number is even or odd (% operator).

# Print the count of even and odd numbers separately.

num_list = [8,4,5,2,9]

even = 0
odd = 0
counter = 1

while counter < len(num_list):
    if num_list[counter] % 2 == 0:
        even = num_list[counter]
        counter += 1
        print(even)
    else:
        odd = num_list[counter]                                    
        counter += 1
        print(odd)
        
        
        
        

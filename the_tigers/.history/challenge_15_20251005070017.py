# Challenge 3: Count Specific Range

# Have a list of numbers.
# Use while loop with index i < len(list).
# Count how many numbers are between 10 and 20 (inclusive).
# Print "Numbers in range 10-20: [count]"

num_list = [3,5,2,8,1,9,10,12,15,17,20]
i = 0
count = 0

while i < len(num_list):
    if num_list[i] >= 10 and num_list[i] <= 20:
       count += 1 
    
    i += 1
    
    print("numbers in range 10-20", count) 
                           
else:
    print("no range between (10-20) found")
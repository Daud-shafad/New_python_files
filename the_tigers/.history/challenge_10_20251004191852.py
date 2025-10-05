# Challenge 3: Find Last Even Number
# Have a list of numbers.
# Use while loop with index i < len(list).
# Print "Last even number: [number]" or "No even numbers" if none found.


num_list = [1,2,5,6,7,8,9,10]

i = len(num_list) - 1

while i >= 0:
    if num_list[i] % 2 == 0:
      print("last even number is: ", num_list[i])
      break 
    i -= 1
    
else:
     print("no even numbers")
    
    

    





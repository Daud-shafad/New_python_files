# Challenge 3: Find Last Even Number
# Have a list of numbers.
# Use while loop with index i < len(list).
# Print "Last even number: [number]" or "No even numbers" if none found.


num_list = [1,2,5,6,7,8,9]

i = 0

while i < len(num_list):
    if num_list[i] % 2 == 0 and num_list[i] == num_list[-1]:
      print("last even number is: ", i)
        
    i +=1

else:
     print("no even numbes")
    





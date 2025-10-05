# Challenge 3: Count Even and Odd Numbers

# Have a list of numbers.

# Use a while loop with index.

# Use if/else to check whether each number is even or odd (% operator).

# Print the count of even and odd numbers separately.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    index += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
        
        
        

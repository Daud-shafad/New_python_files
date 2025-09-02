# Challenge 14: Even or Odd Counter
# Ask the user for numbers until they enter 0.
# Count how many numbers were even and how many were odd, then print the results.

even_count = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
     break
  
    if number % 2 == 0:
     even_count += 1 
     print(f"You entered {even_count} of even numbers")
     odd_count = 0
    elif number % 2 != 0:
     odd_count += 1
     print(f"You entered {odd_count} of odd numbers")
    else:
     print("Invalid number")
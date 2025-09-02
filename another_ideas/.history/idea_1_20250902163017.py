# Challenge 14: Even or Odd Counter
# Ask the user for numbers until they enter 0.
# Count how many numbers were even and how many were odd, then print the results.

count = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
     break
    if number % 2 == 0:
     count += 1
     print(f"You entered {count} of even numbers")
    elif number % 2 != 0:
     count += 1
     print(f"You entered {count} of odd numbers")
    else:
     print("Invalid number")
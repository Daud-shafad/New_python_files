# Challenge 4: Even or Odd Checker

# Ask the user for a number.

# Use if/else and % operator to check if it’s even or odd.

# Print "Even" or "Odd".

# Also check with a boolean variable like is_even = (num % 2 == 0) before using if.

user_number = int(input("Enter a number: "))

is_even = user_number % 2 == 0

if user_number % 2 == 0:
    print("Even")
else:
    print("Odd")




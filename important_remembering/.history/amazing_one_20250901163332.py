#Challenge 1: Odd or Even
# Ask the user for a number and print whether it’s odd or even using if/else.



# Challenge 3: Biggest of Two
# Ask for two numbers and print the bigger one using if/else.

number = int(input("Enter a number: "))
if number > 0 and number % 2 == 0:
    print("Even number")
elif  number > 0 and number % 2 != 0:
    print("Odd number")
else:
    print("Invalid choice")
    

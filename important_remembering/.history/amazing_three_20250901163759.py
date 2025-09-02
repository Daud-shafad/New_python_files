# Challenge 3: Biggest of Two
# Ask for two numbers and print the bigger one using if/else.

number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))

if number_1 > number_2:
    print(number_1)
elif number_2 > number_1:
    print(number_2)
else:
    print("You enter equal numbers.")

# Write a Python program that asks the user to enter an integer.
# If the number is even, print "Even number"; otherwise, print "Odd number".

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
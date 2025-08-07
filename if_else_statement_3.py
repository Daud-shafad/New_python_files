# Write a Python program that asks the user to enter a number.
# If the number is positive, print "Positive".
# If it's negative, print "Negative".
# If it's zero, print "Zero".

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
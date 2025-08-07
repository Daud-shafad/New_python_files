# Write a Python program that keeps asking the user to enter a number until they type 0.
# When 0 is entered, print "Finished" and exit the loop.

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Finished")
        break
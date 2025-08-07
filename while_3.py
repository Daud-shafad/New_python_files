# Create a simple password checker using a while loop.
# Keep asking the user to enter the correct password ("admin123").
# If the entered password is wrong, print "Wrong password, try again."
# When the correct password is entered, print "Access granted" and stop the loop.

while True:
    password = str(input("Enter your correct password: "))
    if password != "admin123":
        print("Wrong password, try again")
    elif password == "admin123":
        print("Access granted")
        break
# Challenge 19: Login System with Allowed Users (if/else + list + while + boolean)

# Have a list of usernames.

# Ask user to enter their name until it matches one from the list.

# Use a boolean flag logged_in to stop the loop.


users = ["ali", "ahmed", "fatima"]

logged_in = False  

while logged_in == False:
    name = input("Enter your username: ")

    if name in users:
        print("Access granted! Welcome,", name)
        logged_in = True
    else:
        print("Username not found. Try again.")

    
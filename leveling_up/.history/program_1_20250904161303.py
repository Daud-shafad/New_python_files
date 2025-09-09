# Challenge 19: Login System with Allowed Users (if/else + list + while + boolean)

# Have a list of usernames.

# Ask user to enter their name until it matches one from the list.

# Use a boolean flag logged_in to stop the loop.

usernames_list = [ "daud", "ahmed", "abdirahman", "mohamed", "hassan" ]
logged_in = True
while True:
    user_choice = input("Enter your username: ").lower()
    if user_choice == usernames_list:
     print("Login successfully")
    if logged_in:
         break
    else:
         print("You enter wrong credentials")
    
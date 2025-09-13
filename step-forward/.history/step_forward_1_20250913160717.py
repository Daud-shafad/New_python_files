# Challenge 1: Login System

# Store usernames and passwords in a dictionary.

# Ask the user for a username and password (input).

# Use if/else to check:

# If the username exists and the password matches → print "Login successful".

# Else → print "Invalid username or password".

usr_pass_dict = {"daud" : "dd123", "muwahib" : "muw123", "maymuna" : "m8910", "usrn1" : "usrn12345" }

user_name = input("Enter a username: ").lower()
user_pass = input("Enter a password: ").lower()

if user_name in usr_pass_dict and usr_pass_dict[user_name] == user_pass:
    print("Login successful")
else:
    print("Invalid username or password")

    
    

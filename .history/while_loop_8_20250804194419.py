# Write a while loop that asks the user to enter a password 
# until the correct password "1234" is entered. 
# When the correct password is entered, print "Access Granted".

while True:
    password = str("Enter your password: ")
    if password == "1234":
        print("Access Granted")
        break
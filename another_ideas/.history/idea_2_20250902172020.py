# Challenge 15: Password Checker
# Ask the user to enter a password until they get it correct. 
# If the password is "python123", print "Access Granted", otherwise keep asking.

while True:
    password = input("Enter a password: ").lower()
    if password == "python123":
        print("Access Granted")
        break
    
        
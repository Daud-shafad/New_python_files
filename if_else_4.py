# Ask the user for a password. If it's "admin123", print "Access Granted", otherwise print "Denied".
password = str(input("Enter the password: "))
if password == "admin123":
    print("Access Granted")
else:
    print("Denied")
    
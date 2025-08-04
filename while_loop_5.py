# Write a program using a while loop that asks the user to enter a password 
# until the correct one ("open123") is entered. When entered correctly, print "Access granted".

while True:
    password = input("Enter your password: ")
    if password == "open123":
        print("Access granted")
        break

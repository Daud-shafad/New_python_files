# Write a program using a while loop that asks the user to enter a password 
# until the correct one ("open123") is entered. When entered correctly, print "Access granted".

i = str(input("Enter your password: "))

while i == "open123":
    print("Access granted")
    break;
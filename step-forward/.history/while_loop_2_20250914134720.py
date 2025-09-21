# Challenge 2: Password Retry

# Ask the user to enter a password.

# Keep asking until they type "python123".

# When correct, print "Access granted".
user_pass = input("Enter a password: ").lower()
while True:
   
    if user_pass == "python123":
        print("Access granted")
        break
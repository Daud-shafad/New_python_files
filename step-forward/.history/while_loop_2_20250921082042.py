# Challenge 2: Password Retry

# Ask the user to enter a password.

# Keep asking until they type "python123".

# When correct, print "Access granted".

while True:
    user_pass = input("Enter a password: ").lower()
    if user_pass == "python123":
        print("Access granted")
        break
    

# Challenge 6: Keep asking until correct password
# password = "admin123"
# user_input = ""
# while user_input != password:
  #  user_input = input("Enter password: ")
# print("Access Granted!")

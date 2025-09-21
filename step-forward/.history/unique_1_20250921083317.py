#🔸 Challenge A: Secret Code Repeater

# There’s a secret code (e.g. "XYZ123").

# Keep asking user to input the code using a while loop.

# Stop when user enters the correct code.

# After correct code, print "Code accepted".

secret_code = "XYZ123"

while True:
    user_code = input("Enter the secret code: ").upper()
    if user_code == "XYZ123":
        print("Code accepted")
        break
    
  
  
  
# THIS IS ANOTHER WAY OF TO CODE THE CHALLENGE  
    
# Challenge A: Secret Code Repeater

# secret_code = "XYZ123"
# user_input = ""

# while user_input != secret_code:
  #  user_input = input("Enter the secret code: ")

# print("Code accepted")

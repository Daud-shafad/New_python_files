# Challenge 1: Keep Asking Name

# Keep asking the user to type their name.

# Stop only when the user types "stop".

# Print "Program ended" at the end.

while True:
    user_name = input("Enter your name type 'stop' to finish: ").lower()
    if user_name == "stop":
        print("Program ended")
        break
# Challenge 5: Infinite Echo

# Keep asking the user to type something.

# Print it back immediately.

# If they type "exit", stop the loop.

while True:
    user_typing = input("Type something: ")
    print(user_typing)
    if user_typing == "exit":
        break
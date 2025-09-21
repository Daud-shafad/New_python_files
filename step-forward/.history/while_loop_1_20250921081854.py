# Challenge 1: Keep Asking Name

# Keep asking the user to type their name.

# Stop only when the user types "stop".

# Print "Program ended" at the end.

while True:
    user_name = input("Enter your name type 'stop' to finish: ").lower()
    if user_name == "stop":
         print("Program ended")
         break
    


# AND YOU CAN WRITE ALSO THIS WAY


# Challenge 8: Keep asking until user says stop
# word = ""
# while word != "stop":
#  word = input("Enter a word (type stop to end): ")
# print("Loop ended!")

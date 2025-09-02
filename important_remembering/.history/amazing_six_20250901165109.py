# Challenge 6: Guess the Number
# Set a secret number (e.g., 7). Keep asking until the user guesses it, then print “Correct!”.

number = 5
while True:
    user_choice = int(input("Enter a number: "))
    if user_choice == number:
        print("correct")
        break
# Challenge 4: Number Guess

# The program has a secret number 7.

# Keep asking the user to guess a number.

# Stop only when they guess 7.

# Then print "You got it!".

sec_num = 7

while True:
    user_num = int(input("Enter a number: "))
    if user_num == 7:
        print("You got it!")
        break
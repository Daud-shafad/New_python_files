# Day 5: Loops + conditions → guess the number game

# The computer secretly picks a random target number.
# Use a loop to repeatedly ask the player for guesses.
# Check each guess with conditions - too high, too low, or correct.
# If correct, celebrate and exit the loop.
# If wrong, give hints and continue until the player succeeds.

secret_number = 23

while True:
    player_number = input("Enter a number to win a prize, type 'stop' to exit: ")
    if player_number == 'stop':
        print("You stopped the game, start it again.")
        break

         
    guess_number = int(player_number)
    
    if guess_number > secret_number:
        print("Too high, try again")
    elif guess_number < secret_number:
        print("Too low, try again")
    elif guess_number == secret_number:
        print("Correct guess, You won.")
        break    
    else:
        print("Wrong Input, Enter a number")
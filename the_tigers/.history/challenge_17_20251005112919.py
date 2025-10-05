# Challenge 2: The Simple Game Menu

# Use a while loop to show a game menu with options: 

# "1. Start Game", "2. Load Game", "3. Options", "4. Exit".

# Use if/else to check if the user wants to exit.

# Use a match statement to handle the other choices (1, 2, 3). 
# For now, each option can just print a message like "Game Starting!" or "Options Menu.".

# If the user enters an invalid choice, tell them.

while True:
    print("\n 1. Start Game")
    print("\n 2. Load Game")
    print("\n 3. Options")
    print("\n 4. Exit")
    
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 4:
        print("Good bye, you skip the game!")
        break
    match user_choice:
        case 1:
            print("Game starting!")
        case 2:
            print("Loading game......")
        case 3:
            print("Options menu")
        case _:
            print("Invalid choice, try again")

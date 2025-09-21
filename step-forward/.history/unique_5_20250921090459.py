# 🔸 Challenge E: Color Matching Game

# Have a tuple of colors (e.g. ("red", "blue", "green", "yellow")).

# Using while loop, ask user to guess a color.

# Use match or if/else to check whether the guessed color is in the tuple.

# If yes, print "You guessed one!".

# If no, print "Try again".

# Stop when user guesses one of the colors correctly.

tuple_colors = ("red", "blue", "green", "yellow")

while True:
    user_color = input("Enter a color: ").lower()
    if user_color in tuple_colors:
        print("You guessed one!")
        break
    else:
        print("Try again")
        

# ANOTHER WAY OF TO CODE THE CHALLENGE


        
# Challenge E: Color Matching Game

# colors = ("red", "blue", "green", "yellow")
# guess = ""

# while guess not in colors:
 #   guess = input("Guess a color: ").lower()
  #  match guess:
   #     case c if c in colors:
    #        print("You guessed one!")
     #   case _:
      #      print("Try again")

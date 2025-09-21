# Challenge 5: Favorite Color Set

# Create a set of colors: {"red", "blue", "green"}.

# Ask the user to input their favorite color.

# Use if/else:

# If it exists in the set → print "Good choice".

# Else → print "Unique choice!".

colors_set = {"red", "blue", "green"}

user_color = input("Enter your favorite color: ").lower()

if user_color in colors_set:
    print("Good choice")
else:
    print("Unique choice")
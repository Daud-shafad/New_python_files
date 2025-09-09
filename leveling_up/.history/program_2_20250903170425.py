# Challenge 20: Favorite Fruits (match + tuple + variable)

# Store fruits in a tuple.

# Ask user for a number (1–3).

# Use match to display which fruit in the tuple they picked.

fruits = ("orange", "apple", "mango")

user_favorite = int(input("Enter a number between 1-3: "))

match user_favorite:
    case 1:
        print("You picked 'Orange'.")
    case 2:
        print("You picked 'Apple'.")
    case 3:
        print("You picked 'Mango'.")  
    case _:
        print("Invalid number, try again.")
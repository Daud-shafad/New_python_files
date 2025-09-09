# Challenge 20: Favorite Fruits (match + tuple + variable)

# Store fruits in a tuple.

# Ask user for a number (1–3).

# Use match to display which fruit in the tuple they picked.

favorite_fruits = ("orange", "apple", "mango")

user_favorite = int(input("Enter a number between 1-3: "))

match user_favorite:
    case 1:
        print("'Orange' is your favorite fruit.")
    case 2:
        print("'Apple' is your favorite fruit.")
    case 3:
        print("'Mango' is your favorite fruit.")  
    case _:
        print("Invalid number, try again.")
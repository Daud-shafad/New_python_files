# Challenge 7: Number Guessing Game
# Combine: numbers, if/else, while, booleans, operators

# Computer picks random number (1-100)

# Player guesses with hints (higher/lower)

# Track attempts and win/lose conditions

user = input("enter a name: ")
match user:
 case usr if usr == "daud" or usr == "iid":
     result = "passed"
     print(result)
 case usr if usr == 'muwahib' or usr == 'hey':
     result = "failed"
     print(result)
     
# Challenge 7: Number Guessing Game
# Combine: numbers, if/else, while, booleans, operators

# Computer picks random number (1-100)

# Player guesses with hints (higher/lower)

# Track attempts and win/lose conditions
import random
print(random.randrange(1,100))
user_track_attempts = []

while True:
  user_number = int(input("Enter a number: "))
  if user_number > random:
      user_track_attempts.append(user_number)
      
      print("Higher guessing")
  elif user_number < random:
      user_track_attempts.append(user_number)
      print("Lower guessing") 
  elif user_number == random:
     user_track_attempts.append(user_number)
     
     print("You got it, You win")
  else:
     print("Invalid input")
     
      

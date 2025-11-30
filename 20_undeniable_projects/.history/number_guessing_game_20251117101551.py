# Challenge 7: Number Guessing Game
# Combine: numbers, if/else, while, booleans, operators

# Computer picks random number (1-100)

# Player guesses with hints (higher/lower)

# Track attempts and win/lose conditions
import random
random_number = random.randrange(1,100)
user_track_attempts = []
attempts = 0

while True:
  user_number = int(input("Enter a number: "))
  if user_number > random_number:
      user_track_attempts.append(user_number)
      print("Higher guessing")
      attempts + 1
  elif user_number < random_number:
      user_track_attempts.append(user_number)
      print("Lower guessing")
      attempts + 1 
  elif user_number == random_number:
      user_track_attempts.append(user_number)
      print("You got it, You win")
      attempts + 1
      print(user_track_attempts)
      print(f"You got it the answer the {attempts} attempt! ")
      break
  else:
     print("Invalid input")
     
      

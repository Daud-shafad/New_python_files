# Challenge 4: Number Guess Statistics

# Generate a secret number (fixed variable) or ask user to input it.

# Let another user guess numbers (while loop).

# Store all guesses in a list.

# Track unique guesses in a set.

# Use casting for number inputs.

# Use operators and booleans to check: guess <, >, or = secret.

# Use if/else or match statement to print hints: "Too high", "Too low", "Correct".

# After correct guess, print statistics tuple: number of attempts, min guess, max guess, average guess.

# Challenge 14: Number Guess Statistics
secret = 15
guesses = []
unique_guesses = set()

guess = -1
while guess != secret:
    guess = int(input("Guess the number: "))
    guesses.append(guess)
    unique_guesses.add(guess)
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")

print("Attempts:", len(guesses))
print("Min guess:", min(guesses))
print("Max guess:", max(guesses))
print("Average guess:", sum(guesses) / len(guesses))
print("Unique guesses:", unique_guesses)
print("Summary Tuple:", (len(guesses), min(guesses), max(guesses)))

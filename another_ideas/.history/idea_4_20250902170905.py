# Challenge 17: Number Guessing (while + if/else)
# Set a secret number (e.g., 7). Use a while loop to ask the user to guess until correct. 
# If guess is too high, print "Too high". If too low, print "Too low".

secret = 6
while True:
 secret_number = int(input("Enter a number: "))
 if secret_number == 5 or secret_number == 7:
     print("Too high")
 elif secret_number == 1 or secret_number == 2:
     print("Too low")
 elif secret_number == 3 or secret_number == 4:
     print("Too low")
 elif secret_number == 8 or secret_number == 9:
     print("Too low")
 elif secret_number == 0:
     print("zero is number but not in here")
     break

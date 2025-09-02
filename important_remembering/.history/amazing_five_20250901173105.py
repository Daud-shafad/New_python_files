# Challenge 5: Sum Until 0
# Keep asking numbers and add them together until the user enters 0, then print the total.
total = 0   # start sum from 0

while True:   # run forever until we break
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break   # stop when user enters 0
    total += number   # add to the running total

print("Total sum:", total)

    
    
    
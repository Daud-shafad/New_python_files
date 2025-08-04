# Create a while loop that keeps asking the user to enter numbers. 
# Stop asking when the user enters a negative number, 
# then print the average of all the entered positive numbers.

i = int(input("Enter a number: "))
while i < 0:
    print(i/i)
    
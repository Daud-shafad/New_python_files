# Create a while loop that keeps asking the user to enter numbers. 
# Stop asking when the user enters a negative number, 
# then print the average of all the entered positive numbers.

total = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average is:", average)
else:
    print("No positive numbers entered")

    
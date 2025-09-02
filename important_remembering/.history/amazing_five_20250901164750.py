# Challenge 5: Sum Until 0
# Keep asking numbers and add them together until the user enters 0, then print the total.

while True:
    number = int(input("Enter a number: "))
    number += number
    print(number)
    if number == 0:
        print(number)
    
    
    
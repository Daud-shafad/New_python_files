# Keep asking the user to enter a number until they type 0. Count how many numbers they entered 
# (excluding the final 0). At the end, print "You entered X numbers".

# (Hint: use a counter variable, e.g. count += 1)

count = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    count+=1
    print(f"You entered {count} numbers")
    

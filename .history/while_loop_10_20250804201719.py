# Write a while loop that starts at 10 and keeps subtracting 1 until it reaches 0. 
# If the current number is odd, skip printing it (use continue).

i = 10
while i >= 0:
    if i % 2 != 0:
        i -= 1
        continue
    print(i)
    i -= 1

    

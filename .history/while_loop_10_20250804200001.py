# Write a while loop that starts at 10 and keeps subtracting 1 until it reaches 0. 
# If the current number is odd, skip printing it (use continue).

i = 10
while i <= 10:
    i-=1
    if i % 2 != 0:
        continue
    print(i)
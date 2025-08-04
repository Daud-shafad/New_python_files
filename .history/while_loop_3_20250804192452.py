# Use a while loop with continue to skip printing number 5 between 1 and 7.
i = 1
while i < 7:
    i+=1
    if i == 5:
       continue
    print(i)

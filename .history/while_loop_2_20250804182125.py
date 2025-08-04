# Write a while loop that prints only the even numbers between 1 and 20.
i = 0
while i < 20:
     print(i)
     if i % 2 == 0:
        i+=2


# Use a while loop with continue to skip printing number 5 between 1 and 7.
i = 1
while i < 7:
    print(i)
    if i == 5:
      continue
i+=1
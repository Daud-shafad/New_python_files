# Use continue to skip printing number 3 in a loop up to 5.

num = 1
while num < 5:
    print(num)
    if num == 3:
     num += 1
     continue
   
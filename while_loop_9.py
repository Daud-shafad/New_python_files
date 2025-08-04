# Write a while loop that prints all the numbers between 50 and 100 (inclusive)
# that are divisible by both 3 and 5.

i = 50
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1
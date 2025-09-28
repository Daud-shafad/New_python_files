# Run an infinite loop with while True, but break at count = 4.

count = 0

while True:
    count += 1
    print(count)
    if count == 4:
        break
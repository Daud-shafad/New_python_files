# Run an infinite loop with while True, but break at count = 4.

count = 0

while True:
    count += 1
    if count == 4:
        print(count)
        break
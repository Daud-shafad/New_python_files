# Keep printing "Running" until a counter reaches 3.

counter = 0
while True:
    print("Running")
    counter += 1
    if counter == 3:
        continue
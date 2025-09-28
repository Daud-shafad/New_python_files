# Keep printing "Running" until a counter reaches 3.

counter = 0
while True:
    counter += 1
    print("running")
    if counter == 3:
        continue
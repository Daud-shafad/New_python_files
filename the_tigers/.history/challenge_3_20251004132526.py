# Challenge 3: Count Even and Odd Numbers

# Have a list of numbers.

# Use a while loop with index.

# Use if/else to check whether each number is even or odd (% operator).

# Print the count of even and odd numbers separately.

num_list = [8,4,5,2,9]

i= 0
c = 0
while True:
    if num_list[0] % 2 == 0:
        i += 1
    elif num_list[0] % 2 != 0:
        c += 1
    elif num_list[1] % 2 == 0:
        i += 1
    elif num_list[1] % 2 != 0:
        c += 1
    elif num_list[2] % 2 == 0:
        i += 1
    elif num_list[2] % 2 != 0:
        c += 1
    elif num_list[3] % 2 == 0:
            i += 1
    elif num_list[3] % 2 != 0:
            c += 1
    elif num_list[4] % 2 == 0:
            i += 1
    elif num_list[4] % 2 != 0:
            c += 1
        
    print(f"even numbers are: {i}, while odd numbers are {c}")
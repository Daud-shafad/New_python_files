# 🔸 Challenge B: Even Number Collector

# Initialize an empty list.

# Using a while loop, keep asking user to enter a number.

# If the number is even, add it to the list.

# Stop input collection when user enters 0.

# After the loop, print the list of collected even numbers.

even_num_collector = []

while True:
    user_number = int(input("Enter a number type '0' to stop/finish: "))
    if user_number % 2 == 0:
        even_num_collector.append(user_number)
        print(even_num_collector)
        break
        
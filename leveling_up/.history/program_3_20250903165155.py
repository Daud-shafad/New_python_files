#Challenge 21: Even Number Collector (while + if/else + list)

# Start with an empty list.

# Keep asking the user for numbers until they enter 0.

# Add only even numbers to the list.

# Print the final list at the end.

my_list = []

while True:
    user_number = int(input("Enter a number: "))
    if user_number == 0:
        break
    if user_number % 2 == 0:
        my_list.append(user_number)
        print(my_list)
 
        
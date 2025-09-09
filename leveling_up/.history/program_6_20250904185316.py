# Challenge 24: Temperature Classifier (while + if/else + list + tuple + variables)

# Start with an empty list to store temperatures.

# Ask the user to enter temperatures repeatedly until they type 0.

# Add each entered temperature into the list.

# After the loop ends, go through the list and classify each temperature:

# If below 15 → "Cold"

# If between 15 and 25 → "Mild"

# If above 25 → "Hot"

# Store the labels in a tuple.

# Finally, print both the temperatures list and the labels tuple.

temp_list = []

while True:
    user_temperature = int(input("Enter a temperature scale type '0' to skip: "))
    print(temp_list.append[user_temperature])
    if user_temperature < 15:
        print("Cold")
    elif user_temperature >= 15 and user_temperature <= 25:
        print("Mild")
    elif user_temperature > 25:
        print("Hot")
        temp_labels = tuple(temp_list)
    else:
        print("Invalid temperature, try again")
        
    print("\n------------final result------------")
    print("Stored temperatures are: " , temp_list + "Celcius")
    print("Labels are: " , temp_labels)
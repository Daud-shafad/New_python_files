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


temps = []  # list to store temperatures
labels = ()  # tuple to store labels
collecting = True  # boolean flag

# collect temperatures
while collecting:
    t = int(input("Enter temperature (0 to stop): "))
    if t == 0:
        collecting = False
    else:
        temps.append(t)

# classify temperatures
i = 0  # index variable
while i < len(temps):
    temp = temps[i]
    match temp:
        case _ if temp < 15:
            labels = labels + ("Cold",)
        case _ if temp <= 25:
            labels = labels + ("Mild",)
        case _:
            labels = labels + ("Hot",)
    i = i + 1

print("Temperatures:", temps)
print("Labels:", labels)

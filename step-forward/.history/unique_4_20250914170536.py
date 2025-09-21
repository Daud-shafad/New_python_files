# 🔸 Challenge D: Unique Names Tracker

# Initialize an empty set.

# Using while loop, keep asking user to input a name.

# If name is "stop", exit loop.

# Otherwise, add the name to the set.

# After loop ends, print all unique names.

unique_names_track = {()}


while True:
    user_name = input("Enter a name: ").lower()
    if user_name == "stop":
       break
    else: 
        unique_names_track.add(user_name)
        
        
print(unique_names_track)


        
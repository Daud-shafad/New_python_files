# 🔹 Challenge Idea: Daily Workout Logger

# 👉 Description:
# Create a program that helps a user track their daily workouts.

# The program should keep asking the user to enter a workout name 
# (like "pushups", "squats", "running") and the number of minutes spent.

# Store the data in a dictionary where the key is the workout name 
# and the value is the total minutes spent on that workout.

# If the user enters the same workout again, 
# add the minutes to the existing total (so it keeps accumulating).

# Stop asking when the user types "stop".

# At the end:

# Print the full workout dictionary.

# Print the total minutes spent on all workouts.

# Print the workout with the maximum minutes (the one they did the most).

user_workout_dict = {}
total = 0

while True:
    user_workout_name = input("Enter a workout name like (pushups, squats, running): ")
    if user_workout_name == "stop":
        break
    user_workout_minutes = int(input("Enter the time you hit the workout in 'minutes': "))
    
    user_workout_dict[user_workout_name] = user_workout_minutes
    if user_workout_name == user_workout_dict.keys():
       total = total + user_workout_minutes
       
print(user_workout_dict)
print(total)
print(max(user_workout_dict.keys()))
    
    
    
# Challenge 4: Temperature Range Checker

# Ask the user to input today’s temperature.

# Store it in a list.

# Use match with guards to classify:

# Below 0 → "Freezing"

# 0–15 → "Cold"

# 16–25 → "Mild"

# 26–35 → "Warm"

# Above 35 → "Hot"

# Use a boolean + operator to check if it’s a “comfortable” range (16–25).

# Print both classification and boolean.

user_temp = int(input("Enter Your Environment's temperature: "))
user_temp_list = []
user_temp_list.append(user_temp)

match user_temp:
    case usrt if usrt < 0:
        classification = "Freezing"
    case usrt if 0 <= usrt <= 15:
        classification = "Cold"
    case usrt if 16 <= usrt <= 25:
        classification = "Mild"
    case usrt if 26 <= usrt <= 35:
        classification = "Warm"
    case usrt if usrt > 35:
        classification = "Hot"

comfortable_temp_checker = user_temp >= 16 <= 25
print("\n---------Final Report----------")
print(user_temp_list)
print("Today is, ", classification)
print("Does today is comfortable temperature, ", comfortable_temp_checker)

# 🔸 Challenge C: Grade Summary

# Keep asking user for grades (numbers 0–100) using while until they enter -1 to stop.

# Use if/else or match to categorize each grade into "pass" (>=60) or "fail" (<60).

# Use a dictionary to count how many passed and how many failed.

# At the end (after -1), print the dictionary: e.g. {"pass": 5, "fail": 2}.
collector_list = []

while True:
    user_grade = int(input("Enter your grade (0-100) type '-1' to stop: "))
    if user_grade == -1:
        break
    match user_grade:
        case usrg if 60 <= usrg <= 100:
            result = "pass"
        case usrg if usrg < 60:
            result = "fail"
        case _:
            result = "Invalid grade"
    collector_list.append(user_grade)
    collector_list.count(user_grade)
    print(collector_list)

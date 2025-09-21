# 🔸 Challenge C: Grade Summary

# Keep asking user for grades (numbers 0–100) using while until they enter -1 to stop.

# Use if/else or match to categorize each grade into "pass" (>=60) or "fail" (<60).

# Use a dictionary to count how many passed and how many failed.

# At the end (after -1), print the dictionary: e.g. {"pass": 5, "fail": 2}.

while True:
    user_grade = int(input("Enter your grade type '-1' to stop: "))
    match user_grade:
        case usrg if 60 <= usrg <= 100:
            result = "pass"
        case usrg if usrg < 60:
            result = "fail"
    pass_collector = sum(60 <= usrg <= 100)
    fail_collector = sum(usrg < 60)
    collector_dict = {}
    collector_dict.update({"pass" : pass_collector, "fail" : fail_collector})
    print(collector_dict)
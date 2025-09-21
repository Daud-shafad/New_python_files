# 🔸 Challenge C: Grade Summary

# Keep asking user for grades (numbers 0–100) using while until they enter -1 to stop.

# Use if/else or match to categorize each grade into "pass" (>=60) or "fail" (<60).

# Use a dictionary to count how many passed and how many failed.

# At the end (after -1), print the dictionary: e.g. {"pass": 5, "fail": 2}.


grades_summary = {"pass": 0, "fail": 0}
grade = 0

while grade != -1:
    grade = int(input("Enter grade (0–100) or -1 to stop: "))
    if grade == -1:
        break
    match grade:
        case g if g >= 60:
            grades_summary["pass"] = grades_summary["pass"] + 1
        case g if g < 60:
            grades_summary["fail"] = grades_summary["fail"] + 1

print("Summary:", grades_summary)

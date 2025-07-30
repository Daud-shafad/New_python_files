name = input("Enter your name")
hours_in_work = float(input("Enter the hours you work in a day "))
days_in_work = float(input("Enter the days you work in a month"))
salary = hours_in_work * days_in_work
print(f"sir! {name}, your salary of this month is, {salary:.2f} USD")
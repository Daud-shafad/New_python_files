"""
    
    🔥 Challenge: BMI Health Classifier

Task: Build a mini BMI calculator and use a match statement with guard conditions to classify the result.

Requirements:

Ask the user for weight (kg) and height (meters).

Compute the BMI using the formula:

BMI   =  weight/ height^2

Use a match statement with guard conditions (case avg if ...) to classify the BMI:

Below 18.5 → "Underweight"

18.5 – 24.9 → "Normal weight"

25 – 29.9 → "Overweight"

30 and above → "Obese"

Use a boolean variable to check if the BMI is healthy (18.5 <= BMI <= 24.9).

Print the BMI, the classification, and whether it’s healthy.
    
"""

user_weight = int(input("Enter your weight as kg: "))
user_height = float(input("Enter you height as meters: "))

user_bmi = (user_weight / (user_weight ** 2))

match user_bmi:
    case bmi if 18.5 > bmi:
        print("Underweight") 
    case bmi if 18.5 <= bmi <= 24.9:
        print("Normal weight")
    case bmi if 25 <= bmi <= 29.9:
        print("Overweight")
    case bmi if 30 < bmi:
        print("Obese")
    
check_bmi = 18.5 <= user_bmi <= 24.9
print("\n-------FINAL REPORT-------")
print(user_bmi)
print(check_bmi)   
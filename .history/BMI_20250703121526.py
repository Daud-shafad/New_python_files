

height_of_person = float(input("enter your height in meters"))
weight_of_person = float(input("enter your weight in kg"))
age = float(input("enter your age"))


body_mass_index = weight_of_person / (height_of_person ** 2)

print(f"your body mass index is, {body_mass_index:.2f} and your age is, {age} years old")
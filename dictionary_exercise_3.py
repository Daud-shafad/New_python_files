# Create a dictionary from two lists:
keys = ["name", "age", "gender"]  
values = ["Ali", 25, "Male"]
mydict = {"name": "Ali", "age" : 25, "gender": "Male"}
print(mydict)

# you can do it also by the below way:
keys_2 = ["name", "age", "gender"]
values_2 = ["Ali", 25, "Male"]
mydict_2 = dict(zip(keys_2, values_2))
print(mydict_2)
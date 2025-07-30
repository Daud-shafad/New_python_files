# Create a dictionary with five fruits as keys and their prices as values. Then increase all prices by 10%.
mydict = {"apple" : 5, "orange" : 4, "banana" : 2, "cherry": 3, "mango" : 6}

price_1 = (5 * 10) / 100
new_apple_price = price_1 + 5
print(new_apple_price)

price_2 = (4 * 10) / 100
new_orange_price = price_2 + 4
print(new_orange_price)

price_3 = (2 * 10) / 100
new_banana_price = price_3 + 2
print(new_banana_price)

price_4 = (3 * 10) / 100
new_cherry_price = price_4 + 3
print(new_cherry_price)

price_5 = (6 * 10) / 100
new_mango_price = price_5 + 6
print(new_mango_price)

mydict = {"apple" : 5.5, "orange" : 4.4, "banana" : 2.2, "cherry": 3.3, "mango" : 6.6}
print(mydict.values())

# or you can do it also by the below way 

fruits = {
    "apple": 5,
    "orange": 4,
    "banana": 2,
    "cherry": 3,
    "mango": 6
}

for fruit in fruits:
    fruits[fruit] = round(fruits[fruit] * 1.10, 2)

print(fruits)
# Output: {'apple': 5.5, 'orange': 4.4, ...}

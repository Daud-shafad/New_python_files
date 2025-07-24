"""
the idea is there is three men who needs to buy a truck car and then the first man has a net worth of 
35,000USD, while the second man has a net worth of 80,000USD and the truck car price was 180,000USD,
in here you have to create a program that prints the net worth of the third man to get the truck car.
"""
first_man = float(input("Enter the net worth of the first man:  "))
second_man = float(input("Enter the net worth of the second man:  "))
truck_car_price = float(input("Enter the price of the truck car they want to buy:  "))
third_man = truck_car_price - (first_man + second_man) 
print(f"The net worth of the third man was, {third_man:.2f} USD")
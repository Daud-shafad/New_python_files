# Convert a tuple (1, 2, 3) into a list, 
# change the 2nd value to 99, and convert it back.

my_tuple = (1,2,3)
my_list = list(my_tuple)
my_list.remove([0])
my_list.insert(1, 99)
my_tuple = tuple(my_list)
print(my_tuple)
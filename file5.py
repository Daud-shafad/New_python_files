# Given t = (1, 2, 3, 4, 5), write code to extract only the first three items into a new tuple.
t = (1, 2, 3, 4, 5)
x = list(t) 
x.remove(4)
new_tuple_1 = tuple(x)
y = list(new_tuple_1)
y.remove(5)
new_tuple_2 = tuple(y)
print(new_tuple_2)


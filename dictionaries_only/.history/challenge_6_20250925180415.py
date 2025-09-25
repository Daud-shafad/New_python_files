# merge keys and values together or merge items in these two dictionaries

dict_1 = {"a" : 20, "b" : 50}
dict_2 = {"c" : 70, "d" : 90}

dict_merge = {**dict_1 , **dict_2}

print(dict_merge)
p
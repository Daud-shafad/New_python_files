# merge keys, also merge values, in these two dictionaries

dict_1 = {"a" : 20, "b" : 50}
dict_2 = {"c" : 70, "d" : 90}

dict_merge_keys = {**dict_1.keys(), **dict_2.keys()}
dict_merge_values = {**dict_1.values(), **dict_2.values()}
print(dict_merge_keys)
print(dict_merge_values)
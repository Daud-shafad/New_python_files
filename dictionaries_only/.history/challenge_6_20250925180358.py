# merge keys and values together or merge items in these two dictionaries

dict_1 = {"a" : 20, "b" : 50}
dict_2 = {"c" : 70, "d" : 90}

dict_merge_keys = {**dict_1 , **dict_2}
dict_merge_values = {**dict_1.values(), **dict_2.values()}
print(dict_merge_keys)
print(dict_merge_values)
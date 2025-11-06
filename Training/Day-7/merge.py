dict1 = { 'x': 10, 'y': 8}
dict2 = { 'a': 6, 'b': 4, 'x': 17}

for i in dict2.keys():
    dict1[i] = dict2[i]

print(dict1)
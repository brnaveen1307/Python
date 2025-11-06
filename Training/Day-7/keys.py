dct = {'a': 1, 'b': 2, 'c': 2}

num = 2

keys = [key for key, val in dct.items() if val == num]
print(keys)
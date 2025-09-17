lst = [1, 2, 2, 3, 3, 3, 4, 5, 4, 3]

unique = set(lst)
for item in unique:
    print(item, ":", lst.count(item))
print(unique)
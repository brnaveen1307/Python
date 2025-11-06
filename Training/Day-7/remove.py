dict1 = {1: 1, 2: 2, 3: 3, 4: 7, 5: 9}
print("Dictionary: ", dict1)

print("dict1.pop(4): ", dict1.pop(4))
print("Updated Dictionary: ", dict1)

print("dict1.popitem: ", dict1.popitem())
print("Updated Dictionary: ", dict1)

dict1.clear() # Clears all the elements in the dictionary

del dict1 # Deletes the dictionary itself
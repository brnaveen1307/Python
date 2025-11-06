dict1 = {1: "Python", 2: "JavaScript", 3: "WebDevelopment", "Name": "Naveen Msd"}
print("Dictionary dict1: ", dict1)

print("dict1[1]: ", dict1[1])
print("dict1[Name]: ", dict1["Name"])


print("dict1.get(2): ", dict1.get(2))
print("dict1.get(5): ", dict1.get(5)) # None
print("dict1.get(3): ", dict1.get(3))

print("dict1[5]: ", dict1[5]) # Key Error
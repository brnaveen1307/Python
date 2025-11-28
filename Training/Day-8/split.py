f = open("myfile1.txt", mode="r")

count = 0
for i in f:
    data = i.split() # Split into words based on spaces and stores in the list
    count += len(data)
    print(data)
print("Count: ", count)
f.close()

f = open("myfile1.txt", mode="r")

data1 = f.readline() # Read First Line
print("Data1: ", data1)

data2 = f.readline() # Read Second Line
print("Data2: ", data2)

f.close()
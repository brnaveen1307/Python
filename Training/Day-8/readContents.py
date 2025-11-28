f = open("myfile1.txt", mode="r")

# data = f.read() # This is for the whole contents
data1 = f.read(5) # First 5 characters from the content
# print("File Contents: \n", data)
print("Data1: ", data1)

data2 = f.read(10) # Next 10 characters from Data1
print("Data2: ", data2)

f.close()
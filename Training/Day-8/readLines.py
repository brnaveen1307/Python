f = open("myfile1.txt", mode="r")

data1 = f.readlines() # Read the whole content in the form of lines and store that in the list
print("Data1: ", data1)

f.close()
f = open("myfile1.txt", mode="r")

num = f.readlines()

lines = len(num)

print("The number of lines: ", lines)

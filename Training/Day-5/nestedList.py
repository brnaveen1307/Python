a = [[0 , 0], [0, 0]]

for i in range(2):
    for j in range(2):
        a[i][j] = (int(input("Enter an element to the list: ")))

print("List: ")
for i in range(2):
    for j in range(2):
        print(a[i][j], end="\t")
    print()
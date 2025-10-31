a = [[0, 0], [0, 0]]
b = [[0, 0], [0, 0]]
c = [[0, 0], [0, 0]]

print("Enter the elements for Matrix A: ")
for i in range(2):
    for j in range(2):
        a[i][j] = int(input("Enter an element to the list: "))

print("Enter the elements for Matrix B: ")
for i in range(2):
    for j in range(2):
        b[i][j] = int(input("Enter an element to the list: "))

print("Enter the elements for Matrix C: ")
for i in range(2):
    for j in range(2):
        c[i][j] = int(input("Enter an element to the list: "))

print("Matrix A: ")
for i in range(2):
    for j in range(2):
        print(a[i][j], end="\t")
    print()

print("Matrix B: ")
for i in range(2):
    for j in range(2):
        print(b[i][j], end="\t")
    print()

print("Matrix C: ")
for i in range(2):
    for j in range(2):
        print(c[i][j], end="\t")
    print()
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

print("Addition of two matrices: ")
for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j] + b[i][j]

print("Resultant Matrix: ")
for i in range(2):
    for j in range(2):
        print(c[i][j], end="\t")
    print()
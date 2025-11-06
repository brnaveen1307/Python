rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialise empty matrices
a = [[0 for j in range(cols)] for i in range(rows)]
b = [[0 for j in range(cols)] for i in range(rows)]
c = [[0 for j in range(cols)] for i in range(rows)]

# Input for Matrix A
print("Enter elements for Matrix A: ")
for i in range(rows):
    for j in range(cols):
        a[i][j] = int(input(f"Enter the element A[{i}][{j}]: "))
        
# Input for Matrix B
print("Enter elements for Matrix B: ")
for i in range(rows):
    for j in range(cols):
        a[i][j] = int(input(f"Enter the element B[{i}][{j}]: "))
                   
# Input for Matrix C
print("Enter elements for Matrix C: ")
for i in range(rows):
    for j in range(cols):
        a[i][j] = int(input(f"Enter the element C[{i}][{j}]: "))  

# Print Matrices
print("Matrix A: ")
for i in range(rows):
    for j in range(cols):
        print(a[i][j], end="\t")
    print() 

print("Matrix B: ")
for i in range(rows):
    for j in range(cols):
        print(b[i][j], end="\t")
    print() 

print("Matrix C: ")
for i in range(rows):
    for j in range(cols):
        print(c[i][j], end="\t")
    print() 
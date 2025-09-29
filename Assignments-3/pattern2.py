# Pattern Printing: Write a code to print the following pattern. 

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

for row in range(1, 5):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()
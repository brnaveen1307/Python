# Pattern Printing: Write a code to print the following pattern. 

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

num = 1
for row in range(1, 5):
    for col in range(row):
        print(num, end=' ')
        num += 1
    print()

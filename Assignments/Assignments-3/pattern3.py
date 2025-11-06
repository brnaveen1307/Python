# Pattern Printing: Write a code to print the following pattern. 

# * * * * 
# * * * 
# * * 
# * 

for row in range(4, 0, -1):
    for col in range(row):
        print("*", end=' ')
    print()
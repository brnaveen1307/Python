# Pattern Printing: A hotel wants to print room numbers in a 5x5 grid (like 101, 102 … 105, 201 … 
# 205, etc.). Use nested loops to generate room numbers.

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}0{j}", end="\t")
    print()

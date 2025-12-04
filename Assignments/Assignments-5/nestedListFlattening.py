# Question 10: Nested List Flattening 
# data = [[1, 2, [3, 4]], [5, 6, [7, 8]]] 

# Tasks: 
# 1. Flatten the list. 
# 2. Double each element. 
# 3. Print sum of all numbers >5. 

# Expected Output: 
# Flattened: [1, 2, 3, 4, 5, 6, 7, 8] 
# Doubled: [2, 4, 6, 8, 10, 12, 14, 16] 
# Sum_Greater_Than_5: 66 

data = [[1, 2, [3, 4]], [5, 6, [7, 8]]]

flat = []
for a, b, c in data:
    flat.append(a)
    flat.append(b)
    flat.extend(c)

doubled = [i * 2 for i in flat]

sum_gt_5 = sum(i for i in doubled if i > 5)

print("Flattened: ", flat)
print("Doubled: ", doubled)
print("Sum_Greater_Than_5: ", sum_gt_5)
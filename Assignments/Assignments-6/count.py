# 6) Word Replacement Count (Merge by Summing) 
# Given: 
# dict1 = {"apple": 5, "banana": 3, "grape": 2} 
# dict2 = {"banana": 4, "grape": 1, "mango": 3} 

# Task: Merge them by summing values of matching keys. 
# Approach: Copy one dict then iterate the other adding values with get().

dict1 = {"apple": 5, "banana": 3, "grape": 2} 
dict2 = {"banana": 4, "grape": 1, "mango": 3} 

final = dict1.copy()

for fruit, count in dict2.items():
    final[fruit] = final.get(fruit, 0) + count
print(final)

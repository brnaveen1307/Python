# Question 1: Inventory Reconciliation 
# Two warehouses contain product IDs. 
# You must print: 
# 1. Items common to both warehouses. 
# 2. Items unique to Warehouse A. 
# 3. Master list (all items, no duplicates, keep A’s order first). 

# Input: 
# warehouse_A = [101, 102, 103, 104, 105, 106] 
# warehouse_B = [105, 106, 107, 108, 109] 

# Expected Output: 
# Common: [105, 106] 
# Unique_A: [101, 102, 103, 104] 
# Master: [101, 102, 103, 104, 105, 106, 107, 108, 109]

warehouse_A = []
for i in range (1, 7):
    a = input("Enter the Product ID's of Warehouse A: ")
    warehouse_A.append(a)
print("Warehouse_A: ", warehouse_A)

warehouse_B = []
for i in range (1, 6):
    b = input("Enter the Product ID's of Warehouse B: ")
    warehouse_B.append(b)
print("Warehouse_B: ", warehouse_B)

common = list(set(warehouse_A) & set(warehouse_B))
print("Common Product IDs:", common)

unique_A = list(set(warehouse_A) - set(warehouse_B))
print("Unique to warehouse A:", unique_A)

warehouse_A = [101, 102, 103, 104]
warehouse_B = [103, 104, 105, 106]

universal = list(set(warehouse_A) | set(warehouse_B))
print("Master:", sorted(universal))
# Question 2: Order Tracker 
# Given an order list with status and price: 

# orders = [ 
# ['order_001', 'shipped', 450], 
# ['order_002', 'pending', 230], 
# ['order_003', 'delivered', 999], 
# ['order_004', 'pending', 350] 
# ] 

# Print: 
# 1. List of pending orders. 
# 2. Total value of shipped + delivered orders. 
# 3. Replace all 'pending' with 'processing' and print updated list. 

# Expected Output: 
# Pending: ['order_002', 'order_004'] 
# Total_Dispatched_Value: 1449 
# Updated_Orders: [['order_001', 'shipped', 450], ['order_002', 'processing', 230], 
# ['order_003', 'delivered', 999], ['order_004', 'processing', 350]]


orders = [ 
    ['order_001', 'shipped', 450], 
    ['order_002', 'pending', 230], 
    ['order_003', 'delivered', 999], 
    ['order_004', 'pending', 350] 
] 


total_cost = []
Pending = []
for i in orders:
    if i[1] == 'pending':
        Pending.append(i[0])
    if i[1] == 'shipped' or i[1] == "delivered":
        total_cost.append(i[2])
        total = sum(total_cost)
    if i[1] == 'pending':
        i[1] = 'processing'

print("Pending: ", Pending)
print("Total_Dispatched_Value: ", total)
print("Updated_Orders: ", orders)
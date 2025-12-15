# 8) Inventory Depletion 
# Given: 
# inventory = {"pen": 50, "book": 20, "eraser": 30} 
# purchase = {"pen": 3, "book": 1} 

# Task: Reduce inventory based on purchase and update remaining stock. 
# Approach: Iterate purchase items and subtract if key exists and enough stock.

inventory = {"pen": 50, "book": 20, "eraser": 30} 
purchase = {"pen": 3, "book": 1} 

for item, qty in purchase.items():
    if item in inventory and inventory[item] >= qty:
        inventory[item] -= qty  

print(inventory)  # Output: {'pen': 47, 'book': 19, 'eraser': 30}
# 13) Remove Items Based on Condition 
# Given: 
# items = {"A": 3, "B": 10, "C": 1, "D": 6} 

# Task: Remove all items whose value is less than 5. 
# Approach: Create new filtered dict or remove keys while iterating over list(items). 

items = {"A": 3, "B": 10, "C": 1, "D": 6} 
filtered_items = {k: v for k, v in items.items() if v >= 5}
print(filtered_items)  # Output: {'B': 10, 'D': 6}
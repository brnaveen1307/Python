# 15) Merge Two Dictionaries (Prefer Second) 
# Given: 
# d1 = {"A": 1, "B": 2} 
# d2 = {"B": 20, "C": 30} 

# Task: Merge them where overlapping keys use value from d2. 
# Approach: Copy d1 then update with d2, or use {**d1, **d2} (d2 overrides). 

d1 = {"A": 1, "B": 2} 
d2 = {"B": 20, "C": 30} 

merged_dict = {**d1, **d2}  # d2 values take precedence
print(merged_dict)  # Output: {'A': 1, 'B': 20, 'C': 30}
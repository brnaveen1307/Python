# 11) Convert Two Lists to Dictionary 
# Given: 
# keys = ["id", "name", "age"] 
# values = [101, "Kumar", 23] 

# Task: Convert both lists into a dictionary. 
# Approach: Use zip(keys, values) and dict().

keys = ["id", "name", "age"] 
values = [101, "Kumar", 23] 

result_dict = dict(zip(keys, values))
print(result_dict)  # Output: {'id': 101, 'name': 'K
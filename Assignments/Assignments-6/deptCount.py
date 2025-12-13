# 10) Employee Department Count 
# Given: 
# departments = {"Mahesh": "IT", "Anu": "HR", "Ravi": "IT", "John": "Finance"}
#  
# Task: Find total number of employees in each department. 
# Approach: Iterate values and count using dict or Counter.

departments = {"Mahesh": "IT", "Anu": "HR", "Ravi": "IT", "John": "Finance"}

dept_count = {} 
for dept in departments.values():
    dept_count[dept] = dept_count.get(dept, 0) + 1  
print(dept_count)  # Output: {'IT': 2, 'HR': 1, 'Finance': 1}
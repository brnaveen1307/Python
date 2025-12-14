# 18) Grouping Names by First Letter 
# Given: 
# names = ["Mahesh", "Manoj", "Anu", "Ankit", "Ravi"] 

# Task: Group names into a dictionary like {'M':['Mahesh','Manoj'],'A':['Anu','Ankit'],'R':['Ravi']} 
# Approach: Iterate names, use first char as key, append to list with setdefault.

names = ["Mahesh", "Manoj", "Anu", "Ankit", "Ravi"] 
grouped_names = {}
for name in names:
    first_char = name[0]
    grouped_names.setdefault(first_char, []).append(name)
print(grouped_names)  # Output: {'M': ['Mahesh', 'Manoj'], 'A': ['Anu', 'Ankit'], 'R': ['Ravi']}
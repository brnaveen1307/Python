# 17) Track Last Occurrence Index 
# Given: 
# list1 = ["apple", "banana", "apple", "grape", "banana"] 

# Task: Create a dict showing each word’s last index in the list. 
# Approach: Enumerate the list and assign index to dict (overwrites older indices). 

list1 = ["apple", "banana", "apple", "grape", "banana"] 
last_index_dict = {}
for index, word in enumerate(list1):
    last_index_dict[word] = index
print(last_index_dict)  # Output: {'apple': 2, 'banana': 4, 'grape': 3}
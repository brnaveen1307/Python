# 16) Counting Even and Odd Occurrences 
# Given: 
# nums = [1,2,3,4,5,6,7,8,2,4,6,2] 

# Task: Create a dictionary showing count of even numbers and odd numbers. 
# Approach: Iterate and check parity, increment counters.

nums = [1,2,3,4,5,6,7,8,2,4,6,2] 
count_dict = {"even": 0, "odd": 0}
for num in nums:
    if num % 2 == 0:
        count_dict["even"] += 1
    else:
        count_dict["odd"] += 1

print(count_dict)  # Output: {'even': 8, 'odd': 4}
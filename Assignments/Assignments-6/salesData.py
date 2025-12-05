# 1) Sales Data Summary 
# Given: 
# sales = {"Jan": 12000, "Feb": 15000, "Mar": 17000, "Apr": 16000} 

# Task: Find the month with the highest sales and the month with the lowest sales. 
# Approach: Use max() and min() with key on dictionary's items to select by value.

sales = {"Jan": 12000, "Feb": 15000, "Mar": 17000, "Apr": 16000} 

maximum = max(sales, key=sales.get)
minimum = min(sales, key=sales.get)

print("Month with Highest Sales: ", maximum)
print("Month with Lowest Sales: ", minimum)
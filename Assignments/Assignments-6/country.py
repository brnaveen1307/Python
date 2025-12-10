# 9) Most Common Country 
# Given: 
# countries = ["India", "USA", "India", "Japan", "USA", "India"] 

# Task: Create a frequency dictionary and find the most frequently occurring country. 
# Approach: Use collections.Counter or manual counting, then max on items. 

countries = ["India", "USA", "India", "Japan", "USA", "India"] 
from collections import Counter

country_count = Counter(countries)
most_common_country = max(country_count.items(), key=lambda x: x[1])    
print(most_common_country)  # Output: ('India', 3)
print(country_count)  # Output: Counter({'India': 3, 'USA': 2, 'Japan': 1})
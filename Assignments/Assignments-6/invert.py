# 12) Invert Dictionary 
# Given: 
# country_capital = {"India": "Delhi", "Japan": "Tokyo", "USA": "Washington"} 

# Task: Swap keys and values → {Capital: Country}. 
# Approach: Use dict comprehension swapping k and v. 

country_capital = {"India": "Delhi", "Japan": "Tokyo", "USA": "Washington"} 

inverted_dict = {v: k for k, v in country_capital.items()}
print(inverted_dict)  # Output: {'Delhi': 'India', 'Tokyo': 'Japan', 'Washington': 'USA'}
# Question 8: Product Price Update 

# products = [ 
# ['Keyboard', 1200], 
# ['Mouse', 500], 
# ['Monitor', 8000], 
# ['Cable', 200], 
# ['Laptop', 55000] 
# ] 

# Rules: - +10% if price < 1000 
#        - +5% otherwise 
# Print updated list and all items with price >5000. 

# Expected Output: 
# Updated_Prices: [['Keyboard', 1260.0], ['Mouse', 550.0], ['Monitor', 8400.0], ['Cable', 
# 220.0], ['Laptop', 57750.0]] 
# Above_5000: ['Monitor', 'Laptop'] 

products = [ 
    ['Keyboard', 1200], 
    ['Mouse', 500], 
    ['Monitor', 8000], 
    ['Cable', 200], 
    ['Laptop', 55000] 
] 

for i in products:
    if i[1] < 1000:
        i[1] += i[1] *  0.1
    else:
        i[1] += i[1] * 0.05

print("Updated_Prices: ", products)

costly = []
for i in products:
    if i[1] > 5000:
        costly.append(i[0])

print("Above_5000: ", costly)
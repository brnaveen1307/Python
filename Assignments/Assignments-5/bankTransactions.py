# Question 4: Bank Transaction Analyzer 
# transactions = [1000, -200, 500, -1500, 2500, -700, 100, -50] 

# Print: 
# 1. Credits and Debits separately. 
# 2. Net Balance. 
# 3. Large movements (>1000 or <-1000). 

# Expected Output: 
# Credits: [1000, 500, 2500, 100] 
# Debits: [-200, -1500, -700, -50] 
# Net_Balance: 1650 
# Large_Movements: [2500, -1500]

transactions = [1000, -200, 500, -1500, 2500, -700, 100, -50]     


credits = []
debits = []
large = []
for i in transactions:
    if i > 0:
        credits.append(i)
    if i < 0:
        debits.append(i)
    if i > 1000 or i < -1000:
        large.append(i)
        large.sort(reverse=True)

print("Credits: ", credits)
print("Debits: ", debits)

balance = sum(transactions)
print("Net_Balance: ", balance)

print("Large_Movements: ", large)
    
def calculate_loss(cost, selling_price):
    if selling_price < cost:
        return cost - selling_price
    else:
        return 0
    
cost = 30000          # cost price of the mobile
selling_price = 22000  # selling price after one year

loss = calculate_loss(cost, selling_price)

print("Loss incurred: ₹", loss)

def calculate_profit(cost, selling_price):
    return selling_price - cost

# Real-world values
cost = 15000          # cost price of the mobile phone
selling_price = 18500 # selling price of the mobile phone

profit = calculate_profit(cost, selling_price)

print(f"Profit earned: ₹{profit}")

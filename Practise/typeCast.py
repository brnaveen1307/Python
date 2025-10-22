# Example: Online Shopping Cart Total Calculation

# Prices coming from a web form or API are often strings
item_price_1 = "499.50"    # price of a headphone
item_price_2 = "299.00"    # price of a mouse
item_price_3 = "1200.75"   # price of a keyboard

# Tax percentage also comes as string from user/admin input
tax_percentage = "18"

# ✅ Type Casting from str → float or int
total = float(item_price_1) + float(item_price_2) + float(item_price_3)
tax_rate = int(tax_percentage) / 100

# Calculate final amount
final_amount = total + (total * tax_rate)

print(f"Total (before tax): ₹{total:.2f}")
print(f"Tax Rate: {tax_rate * 100}%")
print(f"Final Payable Amount: ₹{final_amount:.2f}")

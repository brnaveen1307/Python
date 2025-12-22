def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


price = 2500          # Original price of jacket
discount_percent = 20 # Festival offer

final_price = calculate_discount(price, discount_percent)

print(f"Original Price: ₹{price}")
print(f"Discount: {discount_percent}%")
print(f"Final Price to Pay: ₹{final_price}")

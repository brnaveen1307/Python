# Real-world example: Online Shopping Bill System

# Function to calculate total price of items
def calculate_total(cart):
    total = 0
    for item, price in cart.items():
        total += price
    return total

# Function to apply discount based on total amount
def apply_discount(total):
    if total > 5000:
        return total * 0.90  # 10% discount
    elif total > 2000:
        return total * 0.95  # 5% discount
    else:
        return total

# Function to calculate tax (GST 18%)
def calculate_tax(amount):
    return amount * 0.18

# Function to generate final bill
def generate_bill(cart):
    total = calculate_total(cart)
    discounted_total = apply_discount(total)
    tax = calculate_tax(discounted_total)
    final_amount = discounted_total + tax
    return final_amount

# Customer cart data
shopping_cart = {
    "Shoes": 2500,
    "Watch": 1800,
    "Bag": 1500
}

# Final bill
final_bill = generate_bill(shopping_cart)
print(f"Final Bill Amount (after discount & tax): ₹{final_bill:.2f}")

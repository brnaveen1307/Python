def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

# Real-world values
principal = 50000   # ₹50,000
rate = 6            # 6% per annum
time = 3            # 3 years

interest = calculate_simple_interest(principal, rate, time)
total_amount = principal + interest

print("Simple Interest:", interest)
print("Total Amount after 3 years:", total_amount)

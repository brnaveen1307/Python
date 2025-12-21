def calculate_compound_interest(p, r, t, n):
    amount = p * (1 + r / (100 * n)) ** (n * t)
    return amount

# Real-world usage
principal = 50000     # ₹50,000
rate = 6              # 6% annual interest
time = 3              # 3 years
compounds = 4         # Quarterly compounding

final_amount = calculate_compound_interest(principal, rate, time, compounds)
compound_interest = final_amount - principal

print("Final Amount:", round(final_amount, 2))
print("Compound Interest Earned:", round(compound_interest, 2))

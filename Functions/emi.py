def calculate_emi(principal, rate, months):
    monthly_rate = rate / 12 / 100
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)
    return emi


# Real-world usage
principal = 2500000   # ₹25,00,000
rate = 9              # 9% annual interest
months = 240          # 20 years

emi = calculate_emi(principal, rate, months)

print(f"Your monthly EMI is ₹{emi:.2f}")
